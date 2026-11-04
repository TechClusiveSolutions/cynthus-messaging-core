"""Core Signal Topic class for the Cynthus project"""

from pydantic import BaseModel


class CoreSignalTopic(BaseModel):
    """
        Represents the cynthus-events-topic Azure Service Bus topic

        Domain facts published here are open: any authorized downstream service may consume them.
    """

    name: str = 'cynthus-events-topic'
