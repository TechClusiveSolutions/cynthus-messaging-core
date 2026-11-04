# Meal Domain Signals

The `meal` domain covers the full lifecycle of meal planning, AI-driven suggestions, group voting, user ratings, and recipe associations. All signals in this domain are published to `cynthus-events-topic` and carry the prefix `public.meal.*`.

---

## Aggregates

| Aggregate | Signal prefix | Description |
|---|---|---|
| `plan` | `public.meal.plan.*` | Meal plans scoped to a workspace. |
| `rating` | `public.meal.rating.*` | User ratings (score + optional comment) on a meal entry. |
| `recipes` | `public.meal.recipes.*` | Associations between recipe IDs and a composite meal entry. |
| `suggestion` | `public.meal.suggestion.*` | Astri's AI-driven meal suggestion lifecycle. |
| `tag` | `public.meal.tag.*` | Free-form tags applied to meal entries for preference indexing. |
| `vote` | `public.meal.vote.*` | Group voting on proposed meal choices. |

---

## Suggestion signal flow

The suggestion lifecycle is the most important flow in the meal domain. Understanding the ordering and ownership of each signal is critical for both Core and Intelligence contributors.

```text
[User initiates]
       │
       ▼
cynthus-core-api
  1. Mints context_bundle_id (UUIDv4)
  2. Assembles context bundle:
       - Hard constraints + soft prefs  ← cynthus-profile
       - Inventory snapshot             ← cynthus-inventory
       - Filtered recipe candidates     ← cynthus-recipe
  3. Publishes: public.meal.suggestion.requested
  4. Forwards full bundle to cynthus-chat via VNet peering
       │
       ▼
cynthus-chat (Intelligence subnet — dark)
  5. Generates suggestion using assembled context
  6. Persists to cynthus-intel-db:
       - Context bundle (keyed by context_bundle_id)
       - Suggestion record (keyed by suggestion_id)
       - Meal and recipe references
  7. Publishes: public.meal.suggestion.generated
  8. Returns streaming response to user via cynthus-core-api
       │
       ▼
[User responds]
       │
       ├── Accepts → cynthus-core-api publishes: public.meal.suggestion.accepted
       │
       └── Rejects → cynthus-core-api publishes: public.meal.suggestion.rejected
                     cynthus-core-api triggers a new suggestion round
```

**Key design constraints:**

- `cynthus-chat` **never** calls back into Core services at runtime. The entire context it needs is delivered in the assembled bundle via VNet peering.
- All suggestion detail (meal name, recipe IDs, rationale, spoon cost) is persisted in `cynthus-intel-db` by `cynthus-chat` when the suggestion is generated. Public signals carry only IDs — downstream consumers resolve detail from Intel DB.
- `cynthus-analysis` (also in the Intelligence subnet) resolves `suggestion_id` and `context_bundle_id` against `cynthus-intel-db` directly. It never needs to call Core to build preference models.
- The `context_bundle_id` is the correlation anchor that links the full `requested → generated → accepted/rejected` chain, even though the bundle data itself only ever lives in Intel DB.

---

## Key consumers by signal

| Signal | Key consumers |
|---|---|
| `public.meal.suggestion.requested` | `cynthus-chat` (via VNet, not bus), `cynthus-audit` |
| `public.meal.suggestion.generated` | `cynthus-core-api`, `cynthus-analysis`, `cynthus-notification` |
| `public.meal.suggestion.accepted` | `cynthus-analysis` |
| `public.meal.suggestion.rejected` | `cynthus-core-api` (triggers re-suggestion), `cynthus-analysis` |
| `public.meal.plan.*` | `cynthus-analysis`, `cynthus-scheduler` |
| `public.meal.vote.*` | `cynthus-analysis`, `cynthus-messaging`, `cynthus-notification` |
| `public.meal.rating.*` | `cynthus-analysis` |
| `public.meal.tag.*` | `cynthus-recipe`, `cynthus-analysis` |
| `public.meal.recipes.*` | `cynthus-recipe`, `cynthus-analysis` |
