#!/usr/bin/env python3
""" MRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Put and get to a caching dictionary
    """
    def __init__(self):
        super().__init__()
        self._disc_key = None

    def put(self, key, item):
        """ put key value pair to dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self._disc_key))
                del self.cache_data[self._disc_key]
            self._disc_key = key

    def get(self, key):
        """ return value of key
        """
        item = self.cache_data.get(key)
        if item:
            self._disc_key = key
        return item
