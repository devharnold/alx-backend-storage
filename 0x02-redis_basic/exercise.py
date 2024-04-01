#!/usr/bin/env python3
'''
Writing strings to redis
'''
import redis
import uuid
from typing import Union, Callable, Any, Optional
from redis import Cache
from functools import wraps

cache = Cache()
def count_calls(method: Callable) -> Callable:
    '''Decorator for cache class methods to track call count'''
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        '''Wraps called method and increments call count'''
        self._redis.incr('method.__qualname__')
        return method(self, *args, **kwargs)
    return wrapper

class Cache():
    cache = Cache()
    def __init__(self, _redis=None) -> None:
        '''Constructor for __init__ method'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

    def store(self, value: Union[str, bytes, int]) -> str:
        '''A store method that takes a string and returns a unique identifier'''
        key = self.generate_key()
        self.redis_conn.set(key, value)
        return key

#    def store(self, data: str) -> str:
#        '''A store method that takes a string and returns a unique identifier'''
#        key = str(uuid.uuid4())
#        self._redis.set(key, data)
#
#        return key
    
def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
    '''A get method that takes a key and an optional function and returns the value'''
    value = self.reddis_conn.get(key)
    if value is None:
        return None
    if fn is not None:
        return fn(value)
    return value

def get_str(self, key: str) -> Union[str, bytes, None]:
    '''A get_str method that takes a key and returns the value as a string'''
    return self.get(key, fn=lambda x: x.decode('utf-8'))

def get_int(self, key: str) -> Union[int, bytes, None]:
    '''A get_int method that takes a key and returns the value as an integer'''
    return self.get(key, fn=int)

