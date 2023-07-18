#!/usr/bin/env python3
"""Insert a documnet into mongo using pymongo"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """insrt documents into th emong collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
