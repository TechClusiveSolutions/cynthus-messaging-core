# Identity Access Signals (`audit.identity.access.*`)

An access decision is made each time a service checks a caller token against the permission a request needs.

---

## `audit.identity.access.granted`

**Signal class:** `AuditIdentityAccessGrantedSignal`
**Message class:** `IdentityAccessGrantedMessage`
**Payload class:** `IdentityAccessGrantedPayload`

**Emitted by:** the service that checked the request
**Consumed by:** `cynthus-audit`

**When:** A request is let through. Records who used which permission on which resource.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `user_id` | `str` | Yes | — | The identifier of the user. |
| `token_id` | `Optional[str]` | No | `None` | The identifier of the access token (its jti claim), when it had one. |
| `permission` | `str` | Yes | — | The permission the request needed. |
| `resource` | `str` | Yes | — | The path of the resource that was requested. |
| `method` | `str` | Yes | — | The HTTP method of the request. |

Set the envelope `lifecycle_action` to `created`.

---

## `audit.identity.access.rejected`

**Signal class:** `AuditIdentityAccessRejectedSignal`
**Message class:** `IdentityAccessRejectedMessage`
**Payload class:** `IdentityAccessRejectedPayload`

**Emitted by:** the service that checked the request
**Consumed by:** `cynthus-audit`

**When:** A request has no valid token (missing, malformed, expired, forged or for another caller). Authentication failure (HTTP 401). Lets `cynthus-audit` and security monitoring see attempts without a valid identity.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `reason` | `str` | Yes | — | Why the token was not accepted. |
| `resource` | `str` | Yes | — | The path of the resource that was requested. |
| `method` | `str` | Yes | — | The HTTP method of the request. |

Set the envelope `lifecycle_action` to `created`.

---

## `audit.identity.access.denied`

**Signal class:** `AuditIdentityAccessDeniedSignal`
**Message class:** `IdentityAccessDeniedMessage`
**Payload class:** `IdentityAccessDeniedPayload`

**Emitted by:** the service that checked the request
**Consumed by:** `cynthus-audit`

**When:** A request has a valid token that does not grant the permission it needs. Authorization failure (HTTP 403), the role-based access violation. Lets `cynthus-audit` and security monitoring see users reaching beyond their role.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `user_id` | `str` | Yes | — | The identifier of the user. |
| `token_id` | `Optional[str]` | No | `None` | The identifier of the access token (its jti claim), when it had one. |
| `required_permission` | `str` | Yes | — | The permission the request needed. |
| `granted_permissions` | `List[str]` | No | empty list | The permissions the token carried. |
| `roles` | `List[str]` | No | empty list | The roles the token carried. |
| `resource` | `str` | Yes | — | The path of the resource that was requested. |
| `method` | `str` | Yes | — | The HTTP method of the request. |

Set the envelope `lifecycle_action` to `created`.
