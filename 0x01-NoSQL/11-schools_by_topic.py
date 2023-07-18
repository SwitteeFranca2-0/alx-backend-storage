#!/usr/bin/env python3
"""Schools by topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """return lists of school based on the topic"""
    return list(mongo_collection.find({"topics": {"$all": [topic]}}))
