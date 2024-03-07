#!/usr/bin/python
"""
Module for the user class.
"""
from models.base_model import BaseModel
class user(BaseModel):
    """"
    class user that inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
