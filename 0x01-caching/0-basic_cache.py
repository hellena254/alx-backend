#!/usr/bin/env python3
"""
Basic Cache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the BasicCache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
