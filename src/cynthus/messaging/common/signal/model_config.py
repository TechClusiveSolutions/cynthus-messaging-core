"""Signal Model Config function for the Cynthus project"""

from pydantic import ConfigDict


def create_model_config(frozen: bool = True) -> ConfigDict:
    """Generate and returns a ConfigDict object"""

    config = ConfigDict(
        frozen=frozen,
        populate_by_name=True,
    )

    return config
