#!/usr/bin/env python3
"""
LFU Caching module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements LFU caching.
    """

    def __init__(self):
        """
        Initialize the LFU cache.
        """
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)  # Frequency of access for each key
        self.order = OrderedDict()  # OrderedDict to manage LRU among LFU items

    def put(self, key, item):
        """
        Add an item to the cache using LFU strategy.
        Args:
            key (str): The key for the item.
            item (any): The item to be added to the cache.
        """
        if key and item:
            if key in self.cache_data:
                # Update existing item
                self.cache_data[key] = item
                self.freq[key] += 1
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used items
                    min_freq = min(self.freq.values())
                    lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
                    
                    if len(lfu_keys) > 1:
                        # Use LRU to decide which LFU item to discard
                        lru_key = min(lfu_keys, key=lambda k: self.order[k])
                    else:
                        lru_key = lfu_keys[0]
                    
                    # Discard the least frequently used item
                    print(f"DISCARD: {lru_key}")
                    del self.cache_data[lru_key]
                    del self.freq[lru_key]
                    del self.order[lru_key]

                # Add the new item
                self.cache_data[key] = item
                self.freq[key] = 1
                self.order[key] = None
                self.order.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        Returns:
            The cached item or None if the key is not found.
        """
        if key is None:
            return None
        if key in self.cache_data:
            # Update the frequency and order of access
            self.freq[key] += 1
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
