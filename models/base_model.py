#!/usr/bin/python3
'''
    Write a class BaseModel that defines all
    common attributes/methods for other classes:
'''
import uuid
from datetime import datetime


class BaseModel:
    '''generate class BaseModel'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''function str'''
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.to_dict())

    def save(self):
        '''function that update public instance'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''create dictionnary'''
        dictionnary = self.__dict__.copy()
        dictionnary['__class__'] = type(self).__name__
        dictionnary['created_at'] = self.created_at.isoformat()
        dictionnary['updated_at'] = self.updated_at.isoformat()
        return dictionnary