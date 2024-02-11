#!/usr/bin/python3
""" this is the __init__ magic method for model"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
