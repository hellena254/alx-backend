#!/usr/bin/env python3
"""
FIFO Caching module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements FIFO caching.
    """

    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO strategy.
        
        Args:
            key (str): The key for the item.
            item (any): The item to be added to the cache.
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the first item (FIFO)
                    oldest_key = self.order.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")
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
