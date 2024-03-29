#!/usr/bin/python3
'''Task 9 with mongo db'''

def insert_school(mongo_collection, **kwargs):
    '''insert a document in a collection.
    Arguments:
        mongo_collection {pymongo.collection.Collection} -- The MongoDB collection used in inserting doc.
        **kwargs: The key-value pairs representing the fields to insert.
    Returns:
        str: The inserted doc's ID
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id