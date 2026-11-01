"""Meal Message fixtures for the Cynthus project"""

from pytest import fixture

from ....component.meal.message import (
    MealSuggestionAcceptedMessage,
    MealSuggestionGeneratedMessage,
    MealSuggestionRejectedMessage,
    MealSuggestionRequestedMessage,
)
from ....test.factory.meal import (
    MealSuggestionAcceptedMessageFactory,
    MealSuggestionGeneratedMessageFactory,
    MealSuggestionRejectedMessageFactory,
    MealSuggestionRequestedMessageFactory,
)


@fixture
def meal_suggestion_accepted_message() -> MealSuggestionAcceptedMessage:
    return MealSuggestionAcceptedMessageFactory()


@fixture
def meal_suggestion_generated_message() -> MealSuggestionGeneratedMessage:
    return MealSuggestionGeneratedMessageFactory()


@fixture
def meal_suggestion_rejected_message() -> MealSuggestionRejectedMessage:
    return MealSuggestionRejectedMessageFactory()


@fixture
def meal_suggestion_requested_message() -> MealSuggestionRequestedMessage:
    return MealSuggestionRequestedMessageFactory()
