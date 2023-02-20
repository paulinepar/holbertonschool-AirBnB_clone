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
        self.created_at = self.get_time_iso()
        self.updated_at = self.get_time_iso()

    def get_time_iso(self):
        return str(datetime.isoformat(datetime.now()))

    def __str__(self):
        '''function str'''
        clas = "[{}] ({}) {}".format(type(self).__name__, self.id, self.to_dict())
        return clas

    def save(self):
        '''function that update public instance'''
        self.updated_at = self.get_time_iso()

    def to_dict(self):
        '''create dictionnary'''
        dictionnary = self.__dict__.copy()
        dictionnary['__class__'] = type(self).__name__
        return dictionnary
