#!/usr/bin/env python3
'''
Writing strings to redis
'''
import redis
import uuid
import sys


class Cache():
    def __init__(self, _redis=None) -> None:
        '''Constructor for __init__ method'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

    def store(self, data: str) -> str:
        '''A store method that takes a string and returns a unique identifier'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
    
    def get_str(self, key: str) -> str:
        '''A get method that takes a key and returns the string stored in the key'''
        return self._redis.get(key)
    
    def get_int(self, key: int) -> int:
        '''A get method that takes a key and returns the integer stored in the key'''
        return self._redis.get(key)