#!/usr/bin/python3
"""Module defines class State that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class State - inherits from BaseModel
    Attributes:
        name (str): The name of the state.
    """

    name = ""
