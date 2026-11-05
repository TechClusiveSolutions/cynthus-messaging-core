# Inventory Domain Signals

The `inventory` domain covers storage locations, the shelves within them, and the items held on those shelves. All signals in this domain are published to `cynthus-events-topic` and carry the prefix `public.inventory.*`.

---

## Aggregates

| Aggregate | Signal prefix | Description |
|---|---|---|
| `list` | `public.inventory.list.*` | Request and reply for an inventory listing. |
| `location` | `public.inventory.location.*` | A location is a named physical storage space such as a pantry, fridge or freezer. |
| `shelf` | `public.inventory.shelf.*` | A shelf is a subdivision of a location that holds items and has owners. |
| `item` | `public.inventory.item.*` | An item is a quantity of a product held on a shelf. |

---

## Not yet covered

Shelf ownership and role signals (`audit.inventory.location.role_*`), `public.inventory.mutation.recorded`, low-stock and expiry signals, orders and receipt scans are defined in the signal catalog but have no classes in this package yet.
