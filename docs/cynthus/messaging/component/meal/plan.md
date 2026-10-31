# Meal Plan Signals (`public.meal.plan.*`)

A **meal plan** is a workspace-scoped schedule of meals across a defined horizon (week or month). Plans may be assembled manually or with Astri's assistance.

---

## `public.meal.plan.created`

**Signal class:** `PublicMealPlanCreatedSignal`
**Message class:** `MealPlanCreatedMessage`
**Payload class:** `MealPlanCreatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-analysis`, `cynthus-scheduler`

**When:** A new meal plan is persisted for a workspace.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the plan was created. | `"2026-06-09T09:00:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `plan_id` | `str` | Yes | — | The identifier of the created meal plan. | `"plan_01HXYZABC"` |
| `horizon` | `str` | Yes | — | The planning horizon. | `"week"` or `"month"` |
| `start_date` | `date` | Yes | — | The first date covered by the plan (ISO 8601). | `"2026-06-09"` |
| `end_date` | `date` | Yes | — | The last date covered by the plan (ISO 8601). | `"2026-06-15"` |
| `meal_count` | `int` | Yes | — | The number of meals scheduled within the plan. | `14` |
| `astri_assisted` | `bool` | Yes | — | Whether Astri assisted in assembling the plan. | `true` |

### Wire example

```json
{
  "event_id": "aaaaaaaa-1111-0000-0000-000000000001",
  "event_type": "public.meal.plan.created",
  "lifecycle_action": "created",
  "correlation_id": "cccccccc-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-09T09:00:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T09:00:00.000000+00:00",
    "metadata": {},
    "plan_id": "plan_01HXYZABC",
    "horizon": "week",
    "start_date": "2026-06-09",
    "end_date": "2026-06-15",
    "meal_count": 14,
    "astri_assisted": true
  }
}
```

---

## `public.meal.plan.updated`

**Signal class:** `PublicMealPlanUpdatedSignal`
**Message class:** `MealPlanUpdatedMessage`
**Payload class:** `MealPlanUpdatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-analysis`, `cynthus-scheduler`

**When:** An existing meal plan is modified (e.g. meals added, removed, or rescheduled).

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the update occurred. | `"2026-06-10T11:15:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `plan_id` | `str` | Yes | — | The identifier of the modified meal plan. | `"plan_01HXYZABC"` |
| `updated_fields` | `list[str]` | Yes | — | The names of the plan attributes that changed. Consumers use this to decide whether to invalidate cached state. | `["meal_count", "end_date"]` |

### Wire example

```json
{
  "event_id": "bbbbbbbb-2222-0000-0000-000000000002",
  "event_type": "public.meal.plan.updated",
  "lifecycle_action": "updated",
  "correlation_id": "cccccccc-0000-0000-0000-000000000002",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-10T11:15:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-10T11:15:00.000000+00:00",
    "metadata": {},
    "plan_id": "plan_01HXYZABC",
    "updated_fields": ["meal_count", "end_date"]
  }
}
```

---

## `public.meal.plan.deleted`

**Signal class:** `PublicMealPlanDeletedSignal`
**Message class:** `MealPlanDeletedMessage`
**Payload class:** `MealPlanDeletedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-analysis`, `cynthus-scheduler`

**When:** A meal plan is removed from a workspace.

**Purpose:** Instructs `cynthus-scheduler` to drop any scheduled suggestion deliveries associated with the plan, and notifies `cynthus-analysis` to evict the plan from its working state.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the deletion occurred. | `"2026-06-11T08:00:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `plan_id` | `str` | Yes | — | The identifier of the removed meal plan. | `"plan_01HXYZABC"` |

### Wire example

```json
{
  "event_id": "cccccccc-3333-0000-0000-000000000003",
  "event_type": "public.meal.plan.deleted",
  "lifecycle_action": "deleted",
  "correlation_id": "cccccccc-0000-0000-0000-000000000003",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-11T08:00:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-11T08:00:00.000000+00:00",
    "metadata": {},
    "plan_id": "plan_01HXYZABC"
  }
}
```
