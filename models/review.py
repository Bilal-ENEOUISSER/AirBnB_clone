#!/usr/bin/python
"""
Module for the Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    class Review that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
