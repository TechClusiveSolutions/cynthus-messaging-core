"""Access token issuer for the Cynthus project"""

import base64
import hashlib
import time
from typing import Any, Dict, Iterable
from uuid import UUID

import jwt
from cryptography.hazmat.primitives import serialization
from jwt.algorithms import RSAAlgorithm

ALGORITHM = 'RS256'


class TokenIssuer:
    """Signs access tokens with an RSA private key and publishes the matching public key as a JWKS"""

    def __init__(self, private_key_pem: str | bytes, issuer: str, audience: str, ttl_seconds: int = 900) -> None:
        if isinstance(private_key_pem, str):
            private_key_pem = private_key_pem.encode('utf-8')

        self._private_key = serialization.load_pem_private_key(private_key_pem, password=None)
        self.issuer = issuer
        self.audience = audience
        self.ttl_seconds = ttl_seconds

        public_der = self._private_key.public_key().public_bytes(
            serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.key_id = base64.urlsafe_b64encode(hashlib.sha256(public_der).digest()).decode('ascii').rstrip('=')

    def issue(
        self,
        subject: UUID,
        organization_id: UUID,
        workspace_id: UUID,
        roles: Iterable[str] = (),
        permissions: Iterable[str] = (),
    ) -> str:
        issued_at = int(time.time())

        claims = {
            'iss': self.issuer,
            'aud': self.audience,
            'sub': str(subject),
            'iat': issued_at,
            'exp': issued_at + self.ttl_seconds,
            'organization_id': str(organization_id),
            'workspace_id': str(workspace_id),
            'roles': list(roles),
            'permissions': list(permissions),
        }

        return jwt.encode(claims, self._private_key, algorithm=ALGORITHM, headers={'kid': self.key_id})

    def jwks(self) -> Dict[str, Any]:
        key = RSAAlgorithm.to_jwk(self._private_key.public_key(), as_dict=True)
        key.update({'kid': self.key_id, 'use': 'sig', 'alg': ALGORITHM})

        return {'keys': [key]}
