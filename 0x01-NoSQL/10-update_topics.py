#!/usr/bin/env python3
"""changes all the topics of the school document based on the name"""

def update_topics(mongo_collection, name, topics):
    """
    name (string) will be school name up to update
    topics (list of strings) will be list of topics approached in school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
