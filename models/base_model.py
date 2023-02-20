#!/usr/bin/python3
'''
    Write a class BaseModel that defines all
    common attributes/methods for other classes:
'''
import uuid
import datetime


class BaseModel:
    '''generate class BaseModel'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now())

    def __str__(self):
        '''function str'''
        clas = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return clas

    def save(self):
        '''function that update public instance'''
        self.updated_at = str(datetime.datetime.now())

    def to_dict(self):
        '''create dictionnary'''
        dictionnary = self.__dict__.copy()
        dictionnary['__class__'] = type(self).__name__
        return dictionnary
