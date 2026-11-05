import jwt
from jwt.algorithms import RSAAlgorithm

from cynthus.security import TokenIssuer


def test_a_token_carries_the_identity_and_the_header_names_the_key(issuer, identity):
    token = issuer.issue(**identity, roles=['team_member'], permissions=['inventory:read'])

    header = jwt.get_unverified_header(token)
    claims = jwt.decode(token, options={'verify_signature': False})

    assert header['alg'] == 'RS256' and header['kid'] == issuer.key_id
    assert claims['sub'] == str(identity['subject'])
    assert claims['organization_id'] == str(identity['organization_id'])
    assert claims['workspace_id'] == str(identity['workspace_id'])
    assert (claims['iss'], claims['aud']) == ('cynthus-auth', 'cynthus')
    assert claims['roles'] == ['team_member'] and claims['permissions'] == ['inventory:read']
    assert claims['exp'] - claims['iat'] == 60


def test_the_jwks_holds_the_public_key_that_verifies_the_token(issuer, identity):
    token = issuer.issue(**identity)
    key = issuer.jwks()['keys'][0]

    assert key['kid'] == issuer.key_id and key['use'] == 'sig' and key['alg'] == 'RS256'
    assert 'd' not in key and 'p' not in key
    assert jwt.decode(
        token, RSAAlgorithm.from_jwk(key), algorithms=['RS256'], audience='cynthus', issuer='cynthus-auth'
    )['sub'] == str(identity['subject'])


def test_the_key_id_is_stable_for_the_same_key(private_pem):
    assert TokenIssuer(private_pem, 'a', 'b').key_id == TokenIssuer(private_pem.encode(), 'a', 'b').key_id


def test_different_keys_have_different_ids(private_pem, other_private_pem):
    assert TokenIssuer(private_pem, 'a', 'b').key_id != TokenIssuer(other_private_pem, 'a', 'b').key_id
