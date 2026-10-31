# Meal Tag Signals (`public.meal.tag.*`)

Tags are free-form labels applied to meal entries (e.g. `"quick"`, `"comfort-food"`, `"high-protein"`). They are used by `cynthus-recipe` for preference indexing and by `cynthus-analysis` for lifestyle pattern modelling.

---

## `public.meal.tag.created`

**Signal class:** `PublicMealTagCreatedSignal`
**Message class:** `MealTagCreatedMessage`
**Payload class:** `MealTagCreatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-recipe`, `cynthus-analysis`

**When:** A tag is applied to a meal entry.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the tag was applied. | `"2026-06-09T20:20:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `tag_id` | `str` | Yes | — | The identifier of the created tag record. | `"tag_01HXYZABC"` |
| `meal_id` | `str` | Yes | — | The identifier of the meal the tag was applied to. | `"meal_01HXYZDEF"` |
| `tag` | `str` | Yes | — | The tag value. No enforced normalisation at the signal layer — normalisation is the responsibility of `cynthus-recipe`. | `"quick"` |

### Wire example

```json
{
  "event_id": "kkkkkkkk-bbbb-0000-0000-000000000001",
  "event_type": "public.meal.tag.created",
  "lifecycle_action": "created",
  "correlation_id": "llllllll-0000-0000-0000-000000000001",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-09T20:20:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-09T20:20:00.000000+00:00",
    "metadata": {},
    "tag_id": "tag_01HXYZABC",
    "meal_id": "meal_01HXYZDEF",
    "tag": "quick"
  }
}
```

---

## `public.meal.tag.deleted`

**Signal class:** `PublicMealTagDeletedSignal`
**Message class:** `MealTagDeletedMessage`
**Payload class:** `MealTagDeletedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-recipe`, `cynthus-analysis`

**When:** A tag is removed from a meal entry.

**Purpose:** Notifies `cynthus-recipe` and `cynthus-analysis` to remove the tag from their preference indexes. The `meal_id` is included so consumers can invalidate tag-indexed lookup caches without a separate fetch.

### Payload fields

| Field | Type | Required | Default | Description | Example |
|---|---|---|---|---|---|
| `schema_version` | `int` | Yes | — | Payload schema version. | `1` |
| `observed_at` | `datetime` | No | `utcnow()` | Moment the tag was removed. | `"2026-06-10T10:00:00.000000+00:00"` |
| `metadata` | `dict` | No | `{}` | Non-PII operational telemetry. | `{}` |
| `tag_id` | `str` | Yes | — | The identifier of the removed tag record. | `"tag_01HXYZABC"` |
| `meal_id` | `str` | Yes | — | The identifier of the meal the tag was removed from. | `"meal_01HXYZDEF"` |

### Wire example

```json
{
  "event_id": "mmmmmmmm-cccc-0000-0000-000000000002",
  "event_type": "public.meal.tag.deleted",
  "lifecycle_action": "deleted",
  "correlation_id": "llllllll-0000-0000-0000-000000000002",
  "organization_id": "org_01HXYZABC",
  "workspace_id": "ws_01HXYZ123",
  "actor_id": "usr_01HXYZDEF",
  "timestamp": "2026-06-10T10:00:00.000000+00:00",
  "payload": {
    "schema_version": 1,
    "observed_at": "2026-06-10T10:00:00.000000+00:00",
    "metadata": {},
    "tag_id": "tag_01HXYZABC",
    "meal_id": "meal_01HXYZDEF"
  }
}
```
