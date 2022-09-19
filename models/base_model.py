#!/usr/bin/python3
"""BaseModel modules defines base classes for other classes to inherit"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines common attribtes and methods."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel or create BaseModel from dict

        Args:
            *args (turple): any
            **kwargs (dict): Key/value pairs of attributes.

        Example:
        --------------------------------------
        >>> from models.base_model import BaseModel
        >>> base = BaseModel()
        >>> base.name = "Fat Model"
        >>> base.save()
        >>> base.name
        'Fat Model'
        >>> type(base.id) == str
        True
        >>> len(base.id) == 36
        True
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """ return: [<class name>] (<self.id>) <self.__dict__>

        Example:
        ---------------------------------------
        >>> from models.base_model import BaseModel
        >>> base = BaseModel()
        >>> base.name = "Fat Model"
        >>> base.save()
        >>> string = str(base)
        >>> ('[BaseModel]' in string) == True
        True
        >>> ("Fat Model" in string) == True
        True
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns an instance dictionary keys/values pairs"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
