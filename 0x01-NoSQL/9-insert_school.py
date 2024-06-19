#!/usr/bin/env python3
"""Inserts new document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection will be pymongo collection object
    Returns the new _id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
