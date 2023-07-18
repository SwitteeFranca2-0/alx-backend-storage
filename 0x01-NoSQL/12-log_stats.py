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
    print("{} logs".format(x))
    print("Methods:")
    print("\tmethod GET: {}".format(m_get))
    print("\tmethod POST: {}".format(m_post))
    print("\tmethod PUT: {}".format(m_put))
    print("\tmethod PATCH: {}".format(m_patch))
    print("\tmethod DELETE: {}".format(m_delete))
    print("{} status check".format(get))
