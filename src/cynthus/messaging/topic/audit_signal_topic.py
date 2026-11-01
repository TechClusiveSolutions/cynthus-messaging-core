"""Audit Signal Topic class for the Cynthus project"""

from .signal_topic import SignalTopic


class AuditSignalTopic(SignalTopic):
    """
        Represents the cynthus-topic-audit Azure Service Bus topic

        Append-only compliance and safety events, kept apart from operational traffic.
    """

    name: str = 'cynthus-topic-audit'
