# Meal Vote Signals (`public.meal.vote.*`)

Group meal voting allows workspace members to collectively choose from proposed meal options. A vote session progresses through `initiated → cast (×N) → resolved` or is short-circuited by Astri via `auto_resolved` when a stalemate is detected.

---

## Vote lifecycle

```
cynthus-core-api publishes: public.meal.vote.initiated
        │
        ▼
Members cast votes (one per member)
        │
        ├── Each vote: cynthus-core-api publishes: public.meal.vote.cast
        │
        ▼
Vote closes (deadline reached or unanimous)
        │
        ├── Winner determined → cynthus-core-api publishes: public.meal.vote.resolved
        │
        └── Stalemate → cynthus-chat (Astri) publishes: public.meal.vote.auto_resolved
```

---

## `public.meal.vote.initiated`

**Signal class:** `PublicMealVoteInitiatedSignal`
**Message class:** `MealVoteInitiatedMessage`
**Payload class:** `MealVoteInitiatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-messaging`, `cynthus-notification`, `cynthus-analysis`

**When:** A group meal vote is opened for a workspace.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the vote was opened. | `"2026-06-09T17:00:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `vote_id` | `str` | Yes | — | The identifier of the vote session. | `"vote_01HXYZABC"` |
| `group_id` | `str` | Yes | — | The identifier of the group this vote belongs to. | `"grp_01HXYZ123"` |
| `proposed_meal` | `str` | Yes | — | The display name of the proposed meal. | `"Chicken Stir Fry"` |
| `recipe_id` | `str` | Yes | — | The identifier of the recipe backing the proposed meal. | `"rcp_01HXYZDEF"` |
| `expires_at` | `datetime` | Yes | — | The moment the vote closes. Serialised as ISO 8601 UTC. | `"2026-06-09T17:30:00.000000+00:00"` |

**Serialisation note:** `expires_at` is serialised by a `@field_serializer` that enforces UTC — even if a non-UTC `datetime` is provided at construction, the serialised form will always be UTC.

### Wire example

```json
{
  "event_id": "dddddddd-4444-0000-0000-000000000001",
  "event_type": "public.meal.vote.initiated",
  "lifecycle_action": "created",
  "correlation_id": "eeeeeeee-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-09T17:00:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T17:00:00.000000+00:00",
    "metadata": {},
    "vote_id": "vote_01HXYZABC",
    "group_id": "grp_01HXYZ123",
    "proposed_meal": "Chicken Stir Fry",
    "recipe_id": "rcp_01HXYZDEF",
    "expires_at": "2026-06-09T17:30:00.000000+00:00"
  }
}
```

---

## `public.meal.vote.cast`

**Signal class:** `PublicMealVoteCastSignal`
**Message class:** `MealVoteCastMessage`
**Payload class:** `MealVoteCastPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-analysis`, `cynthus-messaging`

**When:** A group member submits their vote on the proposed meal.

**Purpose:** Updates the running tally for `cynthus-analysis` and `cynthus-messaging`. The `current_tally` snapshot allows consumers to compute the current state without needing to aggregate all prior `cast` events.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the vote was cast. | `"2026-06-09T17:05:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `vote_id` | `str` | Yes | — | The identifier of the vote session. | `"vote_01HXYZABC"` |
| `group_id` | `str` | Yes | — | The identifier of the group this vote belongs to. | `"grp_01HXYZ123"` |
| `vote` | `str` | Yes | — | The voter's submitted choice. | `"yes"`, `"no"`, or `"pending"` |
| `current_tally` | `dict[str, int]` | Yes | — | Running tally of all votes by choice at the moment this vote was cast. Consumers should use this snapshot rather than accumulating totals across events. | `{"yes": 2, "no": 1, "pending": 1}` |

### Wire example

```json
{
  "event_id": "eeeeeeee-5555-0000-0000-000000000002",
  "event_type": "public.meal.vote.cast",
  "lifecycle_action": "updated",
  "correlation_id": "eeeeeeee-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZGHI",
  "timestamp": "2026-06-09T17:05:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T17:05:00.000000+00:00",
    "metadata": {},
    "vote_id": "vote_01HXYZABC",
    "group_id": "grp_01HXYZ123",
    "vote": "yes",
    "current_tally": {"yes": 2, "no": 1, "pending": 1}
  }
}
```

---

## `public.meal.vote.resolved`

**Signal class:** `PublicMealVoteResolvedSignal`
**Message class:** `MealVoteResolvedMessage`
**Payload class:** `MealVoteResolvedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-chat`, `cynthus-notification`, `cynthus-analysis`

**When:** A group meal vote concludes with a clear winning choice (majority or unanimous).

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the vote was resolved. | `"2026-06-09T17:30:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `vote_id` | `str` | Yes | — | The identifier of the concluded vote session. | `"vote_01HXYZABC"` |
| `group_id` | `str` | Yes | — | The identifier of the group this vote belongs to. | `"grp_01HXYZ123"` |
| `resolution` | `str` | Yes | — | The display name of the winning meal choice. | `"Chicken Stir Fry"` |
| `recipe_id` | `str` | Yes | — | The identifier of the recipe backing the winning choice. | `"rcp_01HXYZDEF"` |

### Wire example

```json
{
  "event_id": "ffffffff-6666-0000-0000-000000000003",
  "event_type": "public.meal.vote.resolved",
  "lifecycle_action": "updated",
  "correlation_id": "eeeeeeee-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "svc_cynthus-core-api",
  "timestamp": "2026-06-09T17:30:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T17:30:00.000000+00:00",
    "metadata": {},
    "vote_id": "vote_01HXYZABC",
    "group_id": "grp_01HXYZ123",
    "resolution": "Chicken Stir Fry",
    "recipe_id": "rcp_01HXYZDEF"
  }
}
```

---

## `public.meal.vote.auto_resolved`

**Signal class:** `PublicMealVoteAutoResolvedSignal`
**Message class:** `MealVoteAutoResolvedMessage`
**Payload class:** `MealVoteAutoResolvedPayload`

**Emitted by:** `cynthus-chat`
**Consumed by:** `cynthus-core-api`, `cynthus-notification`, `cynthus-analysis`

**When:** A vote reaches its deadline in a stalemate (tied or insufficient participation) and Astri acts as impartial tiebreaker.

**Purpose:** Distinguished from `vote.resolved` by both the `auto_resolved` action and the `resolved_by` and `tiebreak_rationale` fields, which provide transparency into Astri's decision. `cynthus-notification` uses `tiebreak_rationale` to communicate Astri's reasoning to group members.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment Astri resolved the stalemate. | `"2026-06-09T17:30:05.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `vote_id` | `str` | Yes | — | The identifier of the stalemated vote session. | `"vote_01HXYZABC"` |
| `group_id` | `str` | Yes | — | The identifier of the group this vote belongs to. | `"grp_01HXYZ123"` |
| `resolution` | `str` | Yes | — | The display name of the meal Astri selected. | `"Chicken Stir Fry"` |
| `recipe_id` | `str` | Yes | — | The identifier of the recipe backing Astri's selection. | `"rcp_01HXYZDEF"` |
| `tiebreak_rationale` | `str` | Yes | — | Astri's explanation for the tiebreak decision. Displayed to group members via `cynthus-notification`. | `"Chosen because it uses ingredients expiring today and matches everyone's hard constraints."` |
| `resolved_by` | `str` | Yes | — | The identity of the resolving actor. | `"astri"` |

### Wire example

```json
{
  "event_id": "gggggggg-7777-0000-0000-000000000004",
  "event_type": "public.meal.vote.auto_resolved",
  "lifecycle_action": "updated",
  "correlation_id": "eeeeeeee-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "svc_cynthus-chat",
  "timestamp": "2026-06-09T17:30:05.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T17:30:05.000000+00:00",
    "metadata": {},
    "vote_id": "vote_01HXYZABC",
    "group_id": "grp_01HXYZ123",
    "resolution": "Chicken Stir Fry",
    "recipe_id": "rcp_01HXYZDEF",
    "tiebreak_rationale": "Chosen because it uses ingredients expiring today and matches everyone's hard constraints.",
    "resolved_by": "astri"
  }
}
```
