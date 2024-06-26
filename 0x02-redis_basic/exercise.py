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

def call_history(method: Callable) -> Callable:
    '''Decorator for cache class to track history'''
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        '''Wraps called method and appends to history'''
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper

def replay(fn: Callable) -> None:
    '''Display the history of calls of a particular method'''
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}({input}) -> {output}')

class Cache():
    cache = Cache()
    def __init__(self, _redis=None) -> None:
        '''Constructor for __init__ method'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int]) -> str:
        '''Store data in redis'''
        key = str(uuid.uuid4())
        client = self._redis
        client.set(key, data)
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

