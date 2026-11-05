# Identity Token Signals (`audit.identity.token.*`)

An access token is a signed JWT that proves who a caller is and what they may do.

---

## `audit.identity.token.issued`

**Signal class:** `AuditIdentityTokenIssuedSignal`
**Message class:** `IdentityTokenIssuedMessage`
**Payload class:** `IdentityTokenIssuedPayload`

**Emitted by:** `cynthus-auth`
**Consumed by:** `cynthus-audit`

**When:** An access token is issued. Records which token was issued to whom and with which permissions. The token itself is never included.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `user_id` | `str` | Yes | — | The identifier of the user. |
| `token_id` | `str` | Yes | — | The identifier of the access token (its jti claim). |
| `key_id` | `str` | Yes | — | The identifier of the key that signed the token. |
| `expires_in` | `int` | Yes | — | Seconds until the token expires. |
| `roles` | `List[str]` | No | empty list | The roles carried by the token. |
| `permissions` | `List[str]` | No | empty list | The permissions carried by the token. |

Set the envelope `lifecycle_action` to `created`.
