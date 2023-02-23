#!/usr/bin/python3
""" Doc """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that inherits from BaseMode"""
    
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, value):
        self.email = value
        
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, value):
        self.password = value
    
    @property
    def first_name(self):
        return self.first_name
    
    @first_name.setter
    def first_name(self, value):
        self.first_name = value
    
    @property
    def last_name(self):
        return self.last_name
    
    @last_name.setter
    def last_name(self, value):
        self.last_name = value
