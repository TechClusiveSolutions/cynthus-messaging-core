# Topic Classes

Topic classes are typed wrappers around Azure Service Bus topic names. They are passed into subscription constructors to bind subscriptions to the correct topic.

---

## `CoreSignalTopic`

**Module:** `cynthus.messaging.topic.core_signal_topic`
**Alias:** `PublicTopic` (exported from `cynthus.messaging.topic`)

A Pydantic `BaseModel` wrapping the `cynthus-topic-public` topic name.

| Field | Type | Value |
|---|---|---|
| `name` | `str` | `"cynthus-topic-public"` |

**Usage:** Instantiated inside `PublicSubscription.__init__` and passed to the FastStream broker. Services do not interact with this class directly — it is encapsulated by the subscription layer.

```python
# From PublicSubscription — how CoreSignalTopic is used internally
super().__init__(name=name, topic=PublicTopic(), **kwargs)
```

---

## Topic architecture

The Cynthus platform uses three Service Bus topics. This package currently only covers `cynthus-topic-public`. The internal and audit topics are defined in the private `cynthus-messaging-internal` wheel.

| Topic | Constant | Publisher | Consumers |
|---|---|---|---|
| `cynthus-topic-public` | `CoreSignalTopic` / `PublicTopic` | All open-source Core services | Any authorized service via public subscriptions |
| `cynthus-topic-internal` | *(private wheel)* | Closed-source Intelligence and Health services | Closed-source services only |
| `cynthus-topic-audit` | *(private wheel)* | `cynthus-portal-api`, `cynthus-identity`, `cynthus-profile` | `cynthus-audit` (append-only) |

---

## Adding a new topic

If a future architecture change requires an additional topic (e.g. a dedicated high-throughput telemetry topic):

1. Create `{topic_name}_topic.py` in `src/cynthus/messaging/topic/`.
2. Define a Pydantic model with a `name: str` field defaulting to the Azure topic name.
3. Export from `topic/__init__.py`.
4. Create a corresponding `{service}_{topic}_subscription.py` in `subscription/` that binds to the new topic class.
