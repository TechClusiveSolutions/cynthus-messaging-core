"""Checks the data a request carries against a schema."""

from pydantic import BaseModel, ValidationError

from .api_error import ApiError


class Body:
    @staticmethod
    def validate(schema: type[BaseModel], data: dict) -> BaseModel:
        try:
            return schema.model_validate(data)
        except ValidationError as error:
            raise ApiError.invalid(error) from error

    @staticmethod
    def changes(body: BaseModel) -> dict:
        """The fields the caller sent, leaving out any that were sent as null."""

        return {name: value for name, value in body.model_dump(exclude_unset=True).items() if value is not None}
