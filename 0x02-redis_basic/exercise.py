#!usr/bin/env python3
"""Script that implemnts aacahche claas"""
import redis
import uuid
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """count the number of times a functon is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function for a function decorator"""
        key = method.__qualname__
        data = self._redis.get(key)
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store call history in rredis"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper on method to store inputs and outputs"""
        key = method.__qualname__ + ":inputs"
        self._redis.rpush(key, str(args))
        data = method(self, *args, **kwargs)
        key_out = method.__qualname__ + ":outputs"
        self._redis.rpush(key_out, data)
        return data
    return wrapper


def replay(method: Callable) -> None:
    """Returns the history of calls made to a function"""
    name = method.__qualname__
    r = redis.Redis()
    key = method.__qualname__
    calls = r.get(key).decode("utf-8")
    print("Cache.store was called {} times:".format(calls))
    inputs = r.lrange(key + ":inputs", 0, -1)
    outputs = r.lrange(key + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("Cache.store(*{}) -> {}".format(i.decode('utf-8'),
                                              o.decode('utf-8')))


class Cache:
    """Cahche class for reddis"""

    def __init__(self) -> None:
        """Initialise  the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """store key in redis database"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float, None]:
        """implemment a get fuction which returns data in the desired format"""
        data = self._redis.get(key)
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data

    def get_str(self, key: str):
        """parametarize th ecache.get function with the string conversion"""
        return self._redis.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """parametarize the cane,ge function"""
        return int(self._redis.get(key))
