#!/usr/bin/env python3
""" FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Put and get to a caching dictionary
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key value pair to dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                disc_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(disc_key))
                del self.cache_data[disc_key]

    def get(self, key):
        """ return value of key
        """
        return self.cache_data.get(key)
