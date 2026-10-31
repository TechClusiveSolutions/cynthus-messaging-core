# Subscription Classes

Each service that consumes from `cynthus-topic-public` has a dedicated subscription class. All concrete subscription classes extend `PublicSubscription`, which extends FastStream's `AzureServiceBusSubscription`.

A subscription class's only responsibility is to declare the correct queue name for its service. The topic binding is handled by `PublicSubscription`.

---

## `PublicSubscription`

**Module:** `cynthus.messaging.subscription.public_subscription`

The abstract base for all public-topic subscriptions. Not used directly — subclass it for each consuming service.

```python
class PublicSubscription(AzureServiceBusSubscription):
    def __init__(self, *, name: str, **kwargs) -> None:
        super().__init__(name=name, topic=PublicTopic(), **kwargs)
```

**Topic:** `cynthus-topic-public` (via `CoreSignalTopic`, aliased as `PublicTopic`)

---

## Concrete subscription classes

| Class | Module | Queue name | Consuming service |
|---|---|---|---|
| `AnalysisPublicSubscription` | `subscription.analysis_public_subscription` | `cynthus-analysis-public-sub` | `cynthus-analysis` |
| `AuditPublicSubscription` | `subscription.audit_public_subscription` | `cynthus-audit-public-sub` | `cynthus-audit` |
| `BillingApiPublicSubscription` | `subscription.billing_api_public_subscription` | *(see source)* | `cynthus-billing-api` |
| `ChatPublicSubscription` | `subscription.chat_public_subscription` | `cynthus-chat-public-sub` | `cynthus-chat` |
| `CoreApiSignalSubscription` | `subscription.core_api_signal_subscription` | `cynthus-sub-core-api` | `cynthus-core-api` |
| `CoreCachePublicSubscription` | `subscription.core_cache_public_subscription` | *(see source)* | `cynthus-core-cache` |
| `HealthApiPublicSubscription` | `subscription.health_api_public_subscription` | *(see source)* | `cynthus-health-api` |
| `IdentityPublicSubscription` | `subscription.identity_public_subscription` | *(see source)* | `cynthus-identity` |
| `MessagingPublicSubscription` | `subscription.messaging_public_subscription` | *(see source)* | `cynthus-messaging` |
| `NotificationPublicSubscription` | `subscription.notification_public_subscription` | *(see source)* | `cynthus-notification` |
| `PartnerApiPublicSubscription` | `subscription.partner_api_public_subscription` | *(see source)* | `cynthus-partner-api` |
| `ProfilePublicSubscription` | `subscription.profile_public_subscription` | `cynthus-profile-public-sub` | `cynthus-profile` |
| `RecipePublicSubscription` | `subscription.recipe_public_subscription` | `cynthus-recipe-public-sub` | `cynthus-recipe` |
| `SchedulerPublicSubscription` | `subscription.scheduler_public_subscription` | *(see source)* | `cynthus-scheduler` |
| `ShoppingPublicSubscription` | `subscription.shopping_public_subscription` | *(see source)* | `cynthus-shopping` |

> Several subscription classes are stubs with queue names not yet populated. These are tracked for completion as services are implemented.

---

## Usage in a service

Instantiate the subscription class in the service's FastStream broker setup, then register handlers against it:

```python
from cynthus.messaging.subscription import RecipePublicSubscription

subscription = RecipePublicSubscription()

@broker.subscriber(subscription)
async def handle_meal_tag_created(message: MealTagCreatedMessage) -> None:
    ...
```

---

## Adding a subscription for a new service

1. Create `{service_name}_public_subscription.py` in `src/cynthus/messaging/subscription/`.
2. Subclass `PublicSubscription` and pass the queue name as `name`.
3. Export the class from `subscription/__init__.py`.

Queue names follow the convention `cynthus-{service-name}-public-sub`.

```python
class MyServicePublicSubscription(PublicSubscription):
    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-my-service-public-sub', **kwargs)
```

> **Note:** `CoreApiSignalSubscription` uses a slightly different naming convention (`cynthus-sub-core-api` rather than `cynthus-core-api-public-sub`). New subscriptions should follow the standard `cynthus-{service}-public-sub` pattern.
