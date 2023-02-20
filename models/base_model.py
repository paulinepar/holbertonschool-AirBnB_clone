#!/usr/bin/python3
""" Doc """


import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_ad = datetime.isoformat(datetime.now())
        self.updated_at = datetime.isoformat(datetime.now())

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.isoformat(datetime.now())

    def to_dict(self):
        dictionnary = self.__dict__
        dictionnary['__class__'] = f"{type(self).__name__}"
        return dictionnary
