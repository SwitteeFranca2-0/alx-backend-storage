#!/usr/bin/env python3
"""Update topics in a school document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Update certain topics in school documets"""
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
