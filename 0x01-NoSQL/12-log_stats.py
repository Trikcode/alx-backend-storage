#!/usr/bin/env python3
"""
Module 12-log_stats.py
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    total_gets = nginx_collection.count_documents({"method": "GET"})
    total_posts = nginx_collection.count_documents({"method": "POST"})
    total_puts = nginx_collection.count_documents({"method": "PUT"})
    total_patchs = nginx_collection.count_documents({"method": "PATCH"})
    total_deletes = nginx_collection.count_documents({"method": "DELETE"})
    total_status = nginx_collection.count_documents(
                    {"method": "GET", "path": "/status"})

    print("{} logs".format(total_logs))
    print("Methods:")
    print("\tmethod GET: {}".format(total_gets))
    print("\tmethod POST: {}".format(total_posts))
    print("\tmethod PUT: {}".format(total_puts))
    print("\tmethod PATCH: {}".format(total_patchs))
    print("\tmethod DELETE: {}".format(total_deletes))
    print("{} status check".format(total_status))
