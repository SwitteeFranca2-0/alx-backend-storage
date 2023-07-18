#!/usr/bin/env python3
"""function on log parsing"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx

    x = log_collection.count_documents({})
    m_get = log_collection.count_documents({"method": "GET"})
    m_post = log_collection.count_documents({"method": "POST"})
    m_put = log_collection.count_documents({"method": "PU"})
    m_patch = log_collection.count_documents({"method": "PATCH"})
    m_delete = log_collection.count_documents({"method": "DELETE"})
    get = log_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} logs\nMethods:".format(x))
    print("\tmethod GET: {}\n\tmethod POST: {}".format(m_get, m_post))
    print("\tmethod PUT: {}\n\tmethod PATCH: {}".format(m_put, m_patch))
    print("\tmethod DELETE: {}\n{} status check".format(m_delete, get))
