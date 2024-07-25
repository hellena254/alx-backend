#!/usr/bin/env python3
"""
LRU Caching module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and implements LRU caching.
    """

    def __init__(self):
        """
        Initialize the LRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU strategy.
        Args:
            key (str): The key for the item.
            item (any): The item to be added to the cache.
        """
        if key and item:
            if key in self.cache_data:
                # Update the item and mark it as recently used
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        Returns:
            The cached item or None if the key is not found.
        """
        if key is None:
            return None
        if key in self.cache_data:
            # Mark the item as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
