"""Meal payload part class for the Cynthus project"""

from pydantic import BaseModel, Field
from uuid import UUID


class Meal(BaseModel):
    """Represents a meal object in a signal payload"""
        
    id_: UUID = Field(..., alias='id', description='The meal identifier')
    name: str = Field(..., description='The meal name')
            