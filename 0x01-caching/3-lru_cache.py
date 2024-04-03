
#!/usr/bin/env python3
"""Defining a class LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching"""

    def __init__(self):
        """Initializes a new LRUCache instance"""
        super().__init__()
        self.r_used = []

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the least recently used item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:

