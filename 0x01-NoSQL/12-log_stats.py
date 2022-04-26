#!/usr/bin/env python3
"""
Contains function that provides some stats and more
resent IPS about Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Prints some stats about Nginx logs stored in MongoDB
    and resent most common IPs.
    Args:
        mongo_collection: MongoDB collection object
    Returns:
        Nothing
    """
    num_logs = mongo_collection.count_documents({})
    print("{} logs".format(num_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        docs = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, docs))
    route = mongo_collection.count_documents({"method": "GET",
                                              "path": "/status"})
    print("{} status check".format(route))
    print("IPs:")
    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        log_stats(collection)
