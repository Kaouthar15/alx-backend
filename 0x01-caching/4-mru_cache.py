#!/usr/bin/env python3
"""Defining a class MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.r_used = []

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the most recently used item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:
            return

        if key in self.r_used:
            self.r_used.remove(key)


