#!/usr/bin/python3
""" Doc """


from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self):
        self.name = ""

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value
