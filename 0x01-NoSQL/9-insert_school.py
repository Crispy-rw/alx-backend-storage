#!/usr/bin/env python3
"""
Insert a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs
    Args:
        mongo_collection : pymongo collection object
        kwargs: dict to be added to collection
    """
    doc = {}
    for k, v in kwargs.items():
        doc[k] = v
    result = mongo_collection.insert_one(doc)
    return result.inserted_id
