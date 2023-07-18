#!/usr/bin/python3
"""Module defines class City that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City - inherits from BaseModel
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
