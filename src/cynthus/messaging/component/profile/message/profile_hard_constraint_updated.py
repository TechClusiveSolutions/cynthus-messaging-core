"""ProfileHardConstraintUpdated signal message for the Cynthus project"""

from ....common import AuditProfileHardConstraintUpdatedSignal, SignalMessage
from ..payload import ProfileHardConstraintUpdatedPayload


class ProfileHardConstraintUpdatedMessage(SignalMessage[ProfileHardConstraintUpdatedPayload]):
    """
        Represents a audit.profile.hard_constraint.updated signal message

        Emitted by: `cynthus-profile` when allergies or medical conditions are about to change (published before the change is committed).
        Functional Purpose: Safety-critical audit record of a hard-constraint change (engineering standards section 6); consumed by `cynthus-audit`.
    """

    event_type: str = AuditProfileHardConstraintUpdatedSignal.name
