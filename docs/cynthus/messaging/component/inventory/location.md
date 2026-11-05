# Inventory Location Signals (`public.inventory.location.*`)

A location is a named physical storage space such as a pantry, fridge or freezer.

---

## `public.inventory.location.created`

**Signal class:** `PublicInventoryLocationCreatedSignal`
**Message class:** `InventoryLocationCreatedMessage`
**Payload class:** `InventoryLocationCreatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A new inventory location is created. Lets `cynthus-core-cache` and `cynthus-audit` record the new location.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `location_id` | `str` | Yes | — | The identifier of the location. |
| `name` | `str` | Yes | — | The name of the location. |
| `type` | `str` | Yes | — | The kind of storage space, for example ambient, fridge or freezer. |

Set the envelope `lifecycle_action` to `created`.

### Wire example

```json
{
  "event_type": "public.inventory.location.created",
  "lifecycle_action": "created",
  "payload": {
    "schema_version": 1,
    "location_id": "example",
    "name": "example",
    "type": "example"
  }
}
```

---

## `public.inventory.location.updated`

**Signal class:** `PublicInventoryLocationUpdatedSignal`
**Message class:** `InventoryLocationUpdatedMessage`
**Payload class:** `InventoryLocationUpdatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A location's metadata changes. Lets `cynthus-core-cache` and `cynthus-audit` refresh the location.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `location_id` | `str` | Yes | — | The identifier of the location. |
| `name` | `Optional[str]` | No | `None` | The new name, when it changed. |
| `type` | `Optional[str]` | No | `None` | The new storage type, when it changed. |
| `archived` | `Optional[bool]` | No | `None` | Whether the location is now archived, when that changed. |

Set the envelope `lifecycle_action` to `updated`.

### Wire example

```json
{
  "event_type": "public.inventory.location.updated",
  "lifecycle_action": "updated",
  "payload": {
    "schema_version": 1,
    "location_id": "example",
    "name": "example",
    "type": "example",
    "archived": true
  }
}
```

---

## `public.inventory.location.deleted`

**Signal class:** `PublicInventoryLocationDeletedSignal`
**Message class:** `InventoryLocationDeletedMessage`
**Payload class:** `InventoryLocationDeletedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-shopping`, `cynthus-audit`

**When:** A location is removed. Lets `cynthus-shopping` clear procurement links and `cynthus-core-cache` drop the location.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `location_id` | `str` | Yes | — | The identifier of the location. |

Set the envelope `lifecycle_action` to `deleted`.

### Wire example

```json
{
  "event_type": "public.inventory.location.deleted",
  "lifecycle_action": "deleted",
  "payload": {
    "schema_version": 1,
    "location_id": "example"
  }
}
```
