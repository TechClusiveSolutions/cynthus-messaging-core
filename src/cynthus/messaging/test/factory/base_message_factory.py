"""Base message factory class for MealSuggestionAcceptedMessage"""

import factory

from uuid import UUID, uuid4

from ...common.signal import LifecycleAction


class BaseMessageFactory(factory.Factory):
    class Meta:
        pass

    abstract: bool = True
    event_id: UUID = factory.LazyFunction(uuid4)
    correlation_id: UUID = factory.LazyFunction(uuid4)
    actor_id: UUID = factory.LazyFunction(uuid4)
    organization_id: UUID = factory.LazyFunction(uuid4)
    workspace_id: UUID = factory.LazyFunction(uuid4)
        