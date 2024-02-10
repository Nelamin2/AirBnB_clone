#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel)
    """ represents the Place class
    Attributes:
    city_id (str): the id of the city
    user_id (str): the user id.
    name (str): the name of the place
    description (str): discription of gthe place.
    number_rooms (int): the numbers of the room.
    number_bathrooms (int): the number of the bathroom.
    max_guest (int): the maximum number of guests.
price_by_night (int): the prie per night.
latitude (float): represents the latititude
longitude (float): represents the longitude
amenity_ids (list): the list of Amenity.id."""


city_id = ""
user_id = ""
name = ""
description = ""
number_rooms = 0
max_guest = 0
price_by_night = 0
latitude = 0.0
longitude = 0.0
amenity_ids = []
