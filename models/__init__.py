#!/usr/bin/python3
"""Module that imports Filestorage module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
