#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
"""BaseModel Class"""


class BaseModel():
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """create instances"""
        if kwargs:
            for key, value in kwags.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at'not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
                ') ' + str(self.__dict__))
    
    def save(self):
        """updates the updated_at instace tp current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing all keys"""
        base_dict = self.__dict__.copy()
        base_dict.update({"__class__": self.__class__.__name__, 
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            })
        return base_dict
