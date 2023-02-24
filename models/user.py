#!/usr/bin/python3
""" Doc """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that inherits from BaseMode"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
