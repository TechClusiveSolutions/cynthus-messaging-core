"""Core Signal Topic class for the Cynthus project"""

from pydantic import BaseModel


class CoreSignalTopic(BaseModel):
    """
        Represents the cynthus-topic-public Azure Service Bus topic

        Domain facts published here are open: any authorized downstream service may consume them.
    """

    name: str = 'cynthus-topic-public'
    