#!/usr/bin/python3
""" Doc """


from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self):
        self.state_id = ""
        self.name = ""

    @property
    def state_id(self):
        return self.state_id
    
    @state_id.setter
    def state_id(self, state_id):
        self.state_id = state_id

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name
