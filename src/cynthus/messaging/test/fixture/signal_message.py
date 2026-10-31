"""Signal message envelope helper for the Cynthus test fixtures"""

from uuid import uuid4

from ...common.signal import LifecycleAction


def default_envelope(**overrides):
    """Return the envelope fields every signal message needs, with fresh identifiers unless overridden."""

    envelope = {
        'lifecycle_action': LifecycleAction.CREATED,
        'correlation_id': uuid4(),
        'organization_id': uuid4(),
        'workspace_id': uuid4(),
        'actor_id': uuid4(),
    }
    envelope.update(overrides)

    return envelope
