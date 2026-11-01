"""Signal Message Base class for the Cynthus project"""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import Field

from .lifecycle_action import LifecycleAction
from .part import SignalPart


class SignalMessageBase(SignalPart):
    """Base structural model enforcing multi-tenant isolation contexts."""

    event_id: UUID = Field(
        default_factory=uuid4
    )

    event_type: str = Field(..., description="Dot-notated routing string.")
    lifecycle_action: LifecycleAction
    correlation_id: UUID = Field(..., description="CrossServiceCorrelationGuid.")
    organization_id: UUID = Field(..., description="Corporate Tenant boundary identifier.")
    workspace_id: UUID = Field(..., description="Functional Isolation partition tracking key.")
    actor_id: UUID = Field(..., description="The unique system or user identity executing the shift.")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
