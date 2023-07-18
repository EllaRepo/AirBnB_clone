#!/usr/bin/python3
"""Module defines class Review that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review - inherits from BaseModel
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
