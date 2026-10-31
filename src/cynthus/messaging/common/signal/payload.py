"""Signal Payload class for the Cynthus project"""

from datetime import datetime, timezone
from pydantic import Field, field_serializer
from typing import Any, Dict, Optional

from .part import SignalPart


class SignalPayload(SignalPart):
    """
        Represents the payload part of a signal message

        The baseline contract for all inner message data payloads. Guarantees structural auditability across regulated open/closed boundaries.
    """

    schema_version: int = Field(..., 
    ge=1,
    description='Monotonically increasing version tracker for contract evolution'
    )

    observed_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description='The precise moment the underlying fact was generated or observed at the edge'
    )

    metadata: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description='Structured, non-PII operational telemetry tracking data (e.g., execution_ms, retry_count)'
    )


    @field_serializer('observed_at')
    def serialize_observed_at(self, dt: datetime) -> str:
        """Enforces precise UTC ISO 8601 string formatting on the wire."""

        return dt.astimezone(timezone.utc).isoformat()
