# Inventory Shelf Signals (`public.inventory.shelf.*`)

A shelf is a subdivision of a location that holds items and has owners.

---

## `public.inventory.shelf.created`

**Signal class:** `PublicInventoryShelfCreatedSignal`
**Message class:** `InventoryShelfCreatedMessage`
**Payload class:** `InventoryShelfCreatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A new shelf is added to a location. Lets `cynthus-core-cache` and `cynthus-audit` record the new shelf.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `shelf_id` | `str` | Yes | — | The identifier of the shelf. |
| `location_id` | `str` | Yes | — | The identifier of the location. |
| `name` | `str` | Yes | — | The name of the shelf. |
| `position` | `int` | No | `0` | The position of the shelf within its location. |

Set the envelope `lifecycle_action` to `created`.

### Wire example

```json
{
  "event_type": "public.inventory.shelf.created",
  "lifecycle_action": "created",
  "payload": {
    "schema_version": 1,
    "shelf_id": "example",
    "location_id": "example",
    "name": "example",
    "position": 1
  }
}
```

---

## `public.inventory.shelf.updated`

**Signal class:** `PublicInventoryShelfUpdatedSignal`
**Message class:** `InventoryShelfUpdatedMessage`
**Payload class:** `InventoryShelfUpdatedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A shelf's metadata changes. Lets `cynthus-core-cache` and `cynthus-audit` refresh the shelf.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `shelf_id` | `str` | Yes | — | The identifier of the shelf. |
| `location_id` | `str` | Yes | — | The identifier of the location. |
| `name` | `Optional[str]` | No | `None` | The new name, when it changed. |
| `position` | `Optional[int]` | No | `None` | The new position, when it changed. |

Set the envelope `lifecycle_action` to `updated`.

### Wire example

```json
{
  "event_type": "public.inventory.shelf.updated",
  "lifecycle_action": "updated",
  "payload": {
    "schema_version": 1,
    "shelf_id": "example",
    "location_id": "example",
    "name": "example",
    "position": 1
  }
}
```

---

## `public.inventory.shelf.deleted`

**Signal class:** `PublicInventoryShelfDeletedSignal`
**Message class:** `InventoryShelfDeletedMessage`
**Payload class:** `InventoryShelfDeletedPayload`

**Emitted by:** `cynthus-core-api`
**Consumed by:** `cynthus-core-cache`, `cynthus-audit`

**When:** A shelf is removed. Lets `cynthus-core-cache` drop the shelf and its items.

### Payload fields

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `shelf_id` | `str` | Yes | — | The identifier of the shelf. |
| `location_id` | `str` | Yes | — | The identifier of the location. |

Set the envelope `lifecycle_action` to `deleted`.

### Wire example

```json
{
  "event_type": "public.inventory.shelf.deleted",
  "lifecycle_action": "deleted",
  "payload": {
    "schema_version": 1,
    "shelf_id": "example",
    "location_id": "example"
  }
}
```
