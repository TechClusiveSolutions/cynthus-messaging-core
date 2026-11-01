"""Meal payload part class for the Cynthus project"""

from uuid import UUID

from pydantic import BaseModel, Field


class Meal(BaseModel):
    """Represents a meal object in a signal payload"""

    id_: UUID = Field(..., alias='id', description='The meal identifier')
    name: str = Field(..., description='The meal name')
