#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document based on name.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to update.
        name (str): The name of the document used in updating.
        topics (list): The new list of topics.

    Returns:
        None
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )