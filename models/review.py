#!/usr/bin/python3
""" Doc """


from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self):
        self.place_id = None
        self.user_id = None
        self.text = ""
