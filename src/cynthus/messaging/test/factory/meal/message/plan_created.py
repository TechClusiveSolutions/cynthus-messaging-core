"""Fixture factory for MealPlanCreatedMessage.

Usage in a test or conftest::

    import pytest
    from cynthus.messaging.test.fixture.meal.plan_created import (
        meal_plan_created_message,
    )

    # Register as a pytest fixture in conftest.py:
    # pytest.fixture(meal_plan_created_message)

    def test_something(meal_plan_created_message):
        msg = meal_plan_created_message()           # default 7-day Astri-assisted plan
        msg_manual = meal_plan_created_message(astri_assisted=False, meal_count=5)
        msg_month = meal_plan_created_message(
            horizon="month",
            start_date=date(2026, 7, 1),
            end_date=date(2026, 7, 31),
            meal_count=62,
        )

The factory returns a fully validated ``MealPlanCreatedMessage`` instance.
"""

from datetime import date
from uuid import UUID

import pytest

from cynthus.messaging.common.signal.lifecycle_action import LifecycleAction
from cynthus.messaging.component.meal.message.meal_plan_created import (
    MealPlanCreatedMessage,
)
from cynthus.messaging.component.meal.payload.plan.meal_plan_created import (
    MealPlanCreatedPayload,
)
from cynthus.messaging.test.fixture.signal_message import default_envelope

# ---------------------------------------------------------------------------
# Canned scenario — standard 7-day Astri-assisted week plan
# ---------------------------------------------------------------------------
_PLAN_ID = "plan_01FIXTURE0WEEK0001"
_DEFAULT_HORIZON = "week"
_DEFAULT_START = date(2026, 6, 9)
_DEFAULT_END = date(2026, 6, 15)
_DEFAULT_MEAL_COUNT = 21          # 3 meals × 7 days
_DEFAULT_ASTRI_ASSISTED = True


@pytest.fixture
def meal_plan_created_message():
    """Fixture factory for MealPlanCreatedMessage.

    Returns a callable so individual tests can override any field without
    constructing the whole message by hand.

    Default scenario: a 7-day week plan (Mon 9 Jun – Sun 15 Jun 2026),
    21 meals, assembled with Astri's assistance.
    """

    def _factory(
        *,
        plan_id: str = _PLAN_ID,
        horizon: str = _DEFAULT_HORIZON,
        start_date: date = _DEFAULT_START,
        end_date: date = _DEFAULT_END,
        meal_count: int = _DEFAULT_MEAL_COUNT,
        astri_assisted: bool = _DEFAULT_ASTRI_ASSISTED,
        schema_version: int = 1,
        lifecycle_action: LifecycleAction = LifecycleAction.CREATED,
        correlation_id: UUID = None,
        organization_id: str = None,
        workspace_id: str = None,
        actor_id: str = None,
    ) -> MealPlanCreatedMessage:
        envelope = default_envelope(
            lifecycle_action=lifecycle_action,
            **{k: v for k, v in {
                "correlation_id": correlation_id,
                "organization_id": organization_id,
                "workspace_id": workspace_id,
                "actor_id": actor_id,
            }.items() if v is not None},
        )

        payload = MealPlanCreatedPayload(
            schema_version=schema_version,
            plan_id=plan_id,
            horizon=horizon,
            start_date=start_date,
            end_date=end_date,
            meal_count=meal_count,
            astri_assisted=astri_assisted,
        )

        return MealPlanCreatedMessage(**envelope, payload=payload)

    return _factory
