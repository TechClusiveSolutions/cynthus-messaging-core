# Profile Domain Signals

The `profile` domain covers a user's profile: their allergies, likes, dislikes, favorites and medical conditions. The Core API asks the Profile service to create, get, update or delete the caller's own profile with a request signal and gets the answer back as a response signal, so the client is acknowledged at once. A change is followed by a fact, and a sign-in is followed by a snapshot for the Analysis engine.

Allergies and medical conditions are hard constraints. Before a change to them is committed, the Profile service publishes `audit.profile.hard_constraint.updated`. The request, response, fact and snapshot signals are `public.*`; the audit signal is `audit.*` and is consumed by `cynthus-audit`. All are published to `cynthus-events-topic`.

---

## Signals

| Signal | Emitted by | Purpose |
|---|---|---|
| `public.profile.profile.requested` | `cynthus-core-api` | Hands the request to the Profile service so the caller gets an immediate acknowledgement. |
| `public.profile.profile.responded` | `cynthus-profile` | Carries the outcome back to `cynthus-core-api`, which relays it to the caller. |
| `public.profile.profile.created` | `cynthus-profile` | Lets other services know a profile exists. It names which parts were set, not their contents. |
| `public.profile.profile.updated` | `cynthus-profile` | Lets other services know which parts of a profile changed, without the contents. |
| `public.profile.profile.deleted` | `cynthus-profile` | Lets other services drop what they hold for the profile. |
| `public.profile.snapshot.published` | `cynthus-profile` | Pushes the profile (allergies, likes, dislikes, favorites, conditions) to the Analysis engine, which correlates it with shopping and inventory patterns to refine meal suggestions. |
| `audit.profile.hard_constraint.updated` | `cynthus-profile` | Safety-critical audit record of a hard-constraint change (engineering standards section 6); consumed by `cynthus-audit`. |

---

## `public.profile.profile.requested`

**Signal class:** `PublicProfileProfileRequestedSignal`
**Message class:** `ProfileRequestedMessage`
**Payload class:** `ProfileRequestedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-profile`

**When:** A caller asks to create, get, update or delete their profile. Hands the request to the Profile service so the caller gets an immediate acknowledgement.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `operation` | `Literal['create', 'get', 'update', 'delete']` | Yes | — | What to do: create, get, update or delete. |
| `resource_id` | `Optional[str]` | No | `None` | The profile to get, update or delete; omitted means the caller's own. |
| `data` | `Dict[str, Any]` | No | empty | The fields to create or change the profile with. |

Set the envelope `lifecycle_action` to `updated`.

---

## `public.profile.profile.responded`

**Signal class:** `PublicProfileProfileRespondedSignal`
**Message class:** `ProfileRespondedMessage`
**Payload class:** `ProfileRespondedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-core-api`

**When:** It has dealt with a profile request. Carries the outcome back to `cynthus-core-api`, which relays it to the caller.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `operation` | `str` | Yes | — | The operation that was requested. |
| `status` | `int` | Yes | — | 200, 201 or 204 when it worked; 401, 403, 404, 409, 422 or 503 when it did not. |
| `result` | `Optional[Any]` | No | `None` | The profile when it worked. |
| `error` | `Optional[str]` | No | `None` | Why the request failed. |

Set the envelope `lifecycle_action` to `updated`.

---

## `public.profile.profile.created`

**Signal class:** `PublicProfileProfileCreatedSignal`
**Message class:** `ProfileCreatedMessage`
**Payload class:** `ProfileCreatedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A profile is created. Lets other services know a profile exists. It names which parts were set, not their contents.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `profile_id` | `str` | Yes | — | The identifier of the profile. |
| `user_id` | `str` | Yes | — | The identifier of the user the profile belongs to. |
| `changed` | `List[str]` | No | empty list | Which parts changed: display_name, allergies, likes, dislikes, favorites or conditions. |

Set the envelope `lifecycle_action` to `created`.

---

## `public.profile.profile.updated`

**Signal class:** `PublicProfileProfileUpdatedSignal`
**Message class:** `ProfileUpdatedMessage`
**Payload class:** `ProfileUpdatedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A profile is changed. Lets other services know which parts of a profile changed, without the contents.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `profile_id` | `str` | Yes | — | The identifier of the profile. |
| `user_id` | `str` | Yes | — | The identifier of the user the profile belongs to. |
| `changed` | `List[str]` | No | empty list | Which parts changed: display_name, allergies, likes, dislikes, favorites or conditions. |

Set the envelope `lifecycle_action` to `updated`.

---

## `public.profile.profile.deleted`

**Signal class:** `PublicProfileProfileDeletedSignal`
**Message class:** `ProfileDeletedMessage`
**Payload class:** `ProfileDeletedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A profile is deleted. Lets other services drop what they hold for the profile.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `profile_id` | `str` | Yes | — | The identifier of the profile. |
| `user_id` | `str` | Yes | — | The identifier of the user the profile belongs to. |
| `changed` | `List[str]` | No | empty list | Which parts changed: display_name, allergies, likes, dislikes, favorites or conditions. |

Set the envelope `lifecycle_action` to `deleted`.

---

## `public.profile.snapshot.published`

**Signal class:** `PublicProfileSnapshotPublishedSignal`
**Message class:** `ProfileSnapshotPublishedMessage`
**Payload class:** `ProfileSnapshotPublishedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-analysis`

**When:** A user signs in and has a profile. Pushes the profile (allergies, likes, dislikes, favorites, conditions) to the Analysis engine, which correlates it with shopping and inventory patterns to refine meal suggestions.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `user_id` | `str` | Yes | — | The identifier of the user the profile belongs to. |
| `profile` | `Dict[str, Any]` | Yes | — | The whole profile as the Profile service returns it. |
| `reason` | `str` | No | `'authentication'` | Why the snapshot was published. |

Set the envelope `lifecycle_action` to `snapshot`.

---

## `audit.profile.hard_constraint.updated`

**Signal class:** `AuditProfileHardConstraintUpdatedSignal`
**Message class:** `ProfileHardConstraintUpdatedMessage`
**Payload class:** `ProfileHardConstraintUpdatedPayload`

**Emitted by:** `cynthus-profile`
**Consumed by:** `cynthus-audit`

**When:** Allergies or medical conditions are about to change (published before the change is committed). Safety-critical audit record of a hard-constraint change (engineering standards section 6); consumed by `cynthus-audit`.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `user_id` | `str` | Yes | — | The identifier of the user the profile belongs to. |
| `profile_id` | `str` | Yes | — | The identifier of the profile. |
| `kind` | `str` | Yes | — | allergy or condition. |
| `added` | `List[str]` | No | empty list | The entries being added. |
| `removed` | `List[str]` | No | empty list | The entries being removed. |

Set the envelope `lifecycle_action` to `updated`.

---

## Operations and statuses

A request names an `operation`; `data` is what the Profile service reads.

| Operation | `data` | Answer |
|---|---|---|
| `create` | `display_name` and the lists `allergies`, `likes`, `dislikes`, `favorites`, `conditions`; each entry is a name or `{name, detail}` | `201` and the profile; `409` if the user already has one |
| `get` | none | `200` and the profile; `404` if there is none |
| `update` | `display_name`, and per list either a replacement list or `{set, add, remove}` | `200` and the profile |
| `delete` | none | `204` |

Every operation applies to the caller's own profile; a profile is never reached by anyone else. `get` needs `profile:read`, the rest need `profile:write`. Other statuses: `401` (token missing, forged or for another caller), `403` (token lacks the permission), `422` (input rejected), `503` (the audit signal for a hard-constraint change could not be published, so nothing was changed).
