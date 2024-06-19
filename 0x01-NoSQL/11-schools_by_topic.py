#!/usr/bin/env python3
"""returns the list of the school having a specific topic:"""

def schools_by_topic(mongo_collection, topic):
    """
    topic (string) will be the topic searched
    """
    return mongo_collection.find({"topics": topic})
