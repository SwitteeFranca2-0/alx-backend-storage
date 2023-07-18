#!/usr/bin/env python3
"""function on log parsing"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    logs = log_collection.find()
    x = log_collection.count_documents({})
    m_get = log_collection.count_documents({"method": "GET"})
    m_post = log_collection.count_documents({"method": "POST"})
    m_put = log_collection.count_documents({"method": "PU"})
    m_patch = log_collection.count_documents({"method": "PATCH"})
    m_delete = log_collection.count_documents({"method": "DELETE"})
    get = log_collection.count_documents({"method": "GET", "path": "/status"})
    ips_data = {}
    for log in logs:
        if log.get("ip") not in ips_data.keys():
            ips_data[log.get("ip")] = 1
        else:
            ips_data[log.get("ip")] += 1
    print("{} logs\nMethods:".format(x))
    print("\tmethod GET: {}\n\tmethod POST: {}".format(m_get, m_post))
    print("\tmethod PUT: {}\n\tmethod PATCH: {}".format(m_put, m_patch))
    print("\tmethod DELETE: {}\n{} status check\nIPs:".format(m_delete, get))

    for i in range(10):
        ip = max(ips_data.values())
        index = list(ips_data.values()).index(ip)
        address = list(ips_data.keys())[index]
        print("\t{}: {}".format(address, ip))
        del ips_data[address]
