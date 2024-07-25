#!/usr/bin/env python3
"""
MRU Caching module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and implements MRU caching.
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using MRU strategy.
        Args:
            key (str): The key for the item.
            item (any): The item to be added to the cache.
        """
        if key and item:
            if key in self.cache_data:
                # Update the item and mark it as most recently used
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item (last item in OrderedDict)
                discarded_key, _ = self.cache_data.popitem(last=True)
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
            # Mark the item as most recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
