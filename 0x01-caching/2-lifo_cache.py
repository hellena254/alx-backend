#!/usr/bin/env python3
"""
LIFO Caching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements LIFO caching.
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO strategy.
        Args:
            key (str): The key for the item.
            item (any): The item to be added to the cache.
        """
        if key and item:
            if key in self.cache_data:
                # If key already exists, remove it from the order list
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item (LIFO)
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        Returns:
            The cached item or None if the key is not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
