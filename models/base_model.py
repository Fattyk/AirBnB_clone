#!/usr/bin/python3
"""BaseModel defines all common attributes/methods for other classes to inherit"""

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel is a class that defines attributes and methods to be inherited by all other classes"""


    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            self: the object itself
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return: [<class name>] (<self.id>) <self.__dict__>
        Args:
            self: The object itself
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime
        Args:
            self: The object itself
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance
        Args:
            self: The object itself
        """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
