#!/usr/bin/python3
"""Defines the BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class BaseModel - all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes instance.
        Args:
            args: variable args
            kwargs: variable key/value args
        """
        if kwargs:
            for key, value in kwargs.items():
                frmt = "%Y-%m-%dT%H:%M:%S.%f"
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(kwargs[key], frmt)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns instance information
        """
        info = "[{}] ({}) {}"
        return info.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
           __dict__ of the instance
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        return dict_cpy
