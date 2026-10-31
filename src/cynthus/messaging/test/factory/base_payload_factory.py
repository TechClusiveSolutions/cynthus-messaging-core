"""Base payload factory class for MealSuggestionAcceptedMessage"""

import factory


class BasePayloadFactory(factory.Factory):
    class Meta:
        pass

    abstract: bool = True
    schema_version: int = 1
