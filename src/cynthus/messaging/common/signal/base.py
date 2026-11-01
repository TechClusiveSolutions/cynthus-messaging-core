"""Signal Base class for the Cynthus project"""

from typing import Any, ClassVar

from .action_type import SignalActionType
from .domain_type import SignalDomainType


class _SignalMeta(type):
    """Metaclass that exposes a read-only, computed `name` property at the class level."""

    @property
    def name(cls) -> str:
        return f'{cls.visibility}.{cls.domain.value}.{cls.aggregate}.{cls.action.value}'


class SignalBase(metaclass=_SignalMeta):
    """Establishes the typed naming contract for all signals.

    Concrete subclasses must assign `domain`, `aggregate`, and `action`.
    Intermediate base classes must pass `abstract=True` to skip validation.
    """

    visibility: ClassVar[str] = 'public'
    domain: ClassVar[SignalDomainType]
    aggregate: ClassVar[str]
    action: ClassVar[SignalActionType]

    def __init_subclass__(cls, abstract: bool = False, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if not abstract:
            missing = [f for f in ('domain', 'aggregate', 'action') if not hasattr(cls, f)]
            if missing:
                raise TypeError(
                    f'{cls.__name__} must define the following signal component(s): {", ".join(missing)}'
                )
