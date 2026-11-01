"""Internal Signal Topic class for the Cynthus project"""

from .signal_topic import SignalTopic


class InternalSignalTopic(SignalTopic):
    """
        Represents the cynthus-topic-internal Azure Service Bus topic

        Private signals (lifestyle, chat, video, system) that only closed-source services consume.
    """

    name: str = 'cynthus-topic-internal'
