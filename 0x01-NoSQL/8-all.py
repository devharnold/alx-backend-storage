#!/usr/bin/python3
'''Task 8 with mongo db'''

def list_all(mongo_collection):
    '''list all documents in a collection.
    Arguments:
        mongo_collection {pymongo collection object} -- collection to use.
    Returns:
        list: A list of all documents in the collection.
    '''
    return [doc for doc in mongo_collection.find()]