#!/usr/bin/env python3
""" Basic caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Put and get to a caching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key value pair to dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return value of key
        """
        return self.cache_data.get(key)
