# Inventory Request and Response Signals

Every request to change or read inventory records travels as a signal, so the caller gets an immediate acknowledgement and the answer arrives asynchronously. The Core API publishes a `requested` signal and relays the matching `responded` signal to the caller, joined by the envelope `correlation_id`.

| Aggregate | Request | Response |
|---|---|---|
| `location` | `public.inventory.location.requested` | `public.inventory.location.responded` |
| `shelf` | `public.inventory.shelf.requested` | `public.inventory.shelf.responded` |
| `item` | `public.inventory.item.requested` | `public.inventory.item.responded` |
| `owner` | `public.inventory.owner.requested` | `public.inventory.owner.responded` |

Emitted by: the request by `cynthus-core-api`, the response by `cynthus-inventory`. Both carry the caller's `organization_id`, `workspace_id` and `actor_id`. The request travels with the caller's access token in the `authorization` message property, and the Inventory service refuses a request whose token is not genuine, lacks the permission, or names another caller.

---

## Request payload

`InventoryRequestedPayload` is shared by the four request signals.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `operation` | `str` | Yes | — | `create`, `get`, `list`, `update` or `delete`. |
| `resource_id` | `str` | No | `None` | The record to get, update or delete. |
| `parent_id` | `str` | No | `None` | The shelf an owner belongs to. |
| `filters` | `dict` | No | empty | Narrows a list, for example `type`, `name`, `location_id` or `shelf_id`. |
| `data` | `dict` | No | empty | The fields to create or change a record with. |

Reads (`get`, `list`) need the permission `inventory:read`; `create`, `update` and `delete` need `inventory:write`. For an owner, `create` adds the user in `data.owner_id` to the shelf in `parent_id`, `list` lists the owners of that shelf, and `delete` removes the owner in `resource_id` from it.

## Response payload

`InventoryRespondedPayload` is shared by the four response signals.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `schema_version` | `int` | No | `1` | Payload schema version. |
| `operation` | `str` | Yes | — | The operation that was requested. |
| `status` | `int` | Yes | — | `200`, `201` or `204` when it worked; `401`, `403`, `404`, `409` or `422` when it did not. |
| `result` | `Any` | No | `None` | The record, or the list of records, when it worked. |
| `error` | `str` | No | `None` | Why it failed. |

A record in another workspace is reported as `404`, never `403`.

## Wire example

```json
{
  "event_type": "public.inventory.location.requested",
  "lifecycle_action": "updated",
  "payload": {
    "schema_version": 1,
    "operation": "create",
    "data": { "name": "Chest freezer", "type": "frozen" }
  }
}
```
