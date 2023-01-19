#!/usr/bin/env python3
"""Create a Cache class. In the
__init__ method, store an instance of
the Redis client as a private variable
named _redis (using redis.Redis())
and flush the instance using flushdb.
"""
import redis
import uuid
from typing import Union, Optional


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """ storing an instance of the
        Redis client as a private variable
        named _redis"""
        r = redis.Redis()
        self.__redis = r
        self.__redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """generate a random key,
        store the input data in Redis using
        the random key and return the key"""
        rid = str(uuid.uuid4())
        self.__redis.set(rid, data)
        return rid

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, float, int]:
        """Get stored value back"""
        v = self.__redis.get(key)
        if not fn:
            return v
        else:
            return fn(v)  

    def get_str(self, key: str) -> str:
        """get string"""
        v = self.__redis.get(key).decode("utf-8")
        return v

    def get_int(self, key: str) -> int:
        """get int"""
        v = self.__redis.get(key)
        if type(v) is int:
            return v
