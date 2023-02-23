#!/usr/bin/python3
'''
    Write a class BaseModel that defines all
    common attributes/methods for other classes:
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''generate class BaseModel'''
    def __init__(self, *args, **kwargs):
        
        if not kwargs or type(kwargs) is not dict:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            self.update(kwargs)
        



    def update(self, kwargs):
        if kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k,  v)

    def __str__(self):
        '''function str'''
        d = self.to_dict().copy();
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, d)

    def save(self):
        '''function that update public instance'''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''create dictionnary'''
        dictionnary = self.__dict__.copy()

        dictionnary['__class__'] = "BaseModel"
        dictionnary['created_at'] = self.created_at.isoformat()
        dictionnary['updated_at'] = self.updated_at.isoformat()
        return dictionnary