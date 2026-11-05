# Access Token Security (`cynthus.security`)

Services trust the signed access token only (engineering standards, section 4). This package issues those tokens and verifies them, so every service checks them the same way.

---

## Classes

| Class | Used by | Purpose |
|---|---|---|
| `TokenIssuer` | `cynthus-auth` | Signs access tokens with an RSA private key (RS256) and publishes the public key as a JWKS. |
| `TokenVerifier` | API, Inventory and other services | Fetches the JWKS and checks the signature, issuer, audience and expiry of a token. |
| `TokenClaims` | all | The verified identity: user, `organization_id`, `workspace_id`, roles and permissions. |
| `BearerToken` | services that read HTTP headers or message properties | Extracts the token from an `Authorization: Bearer <token>` value. |
| `TokenError` | all | Raised for any token that is missing, malformed, expired or not trusted. Carries a short `reason`. |

---

## Token contents

| Claim | Meaning |
|---|---|
| `iss` | Issuer. Defaults to `cynthus-auth`. |
| `aud` | Audience. Defaults to `cynthus`. |
| `sub` | The user's id. |
| `iat`, `exp` | Issue and expiry times, in seconds since the epoch. |
| `organization_id`, `workspace_id` | The tenant the token is valid for. Required. |
| `roles` | Roles granted to the user, for example `workspace_administrator`. |
| `permissions` | What the token may do, for example `inventory:read` and `inventory:write`. |

A token that lacks `exp`, `iat`, `sub`, `iss`, `aud`, `organization_id` or `workspace_id` is rejected. Only RS256 is accepted, so an unsigned token or one signed with a shared secret never verifies.

---

## Verifier settings

`TokenVerifier.from_environment()` reads these variables:

| Variable | Default |
|---|---|
| `AUTH_JWKS_URL` | `http://auth:8000/.well-known/jwks.json` |
| `AUTH_ISSUER` | `cynthus-auth` |
| `AUTH_AUDIENCE` | `cynthus` |

The keys are cached and fetched again when a token names a key id that is not cached, so a key rotation needs no restart.

---

## Example

```python
verifier = TokenVerifier.from_environment()

try:
    claims = await verifier.verify(BearerToken.extract(request.headers.get('authorization')))
except TokenError as error:
    ...  # respond 401 with {"error": error.reason}

if not claims.has_permission('inventory:read'):
    ...  # respond 403
```
