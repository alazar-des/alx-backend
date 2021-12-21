#!/usr/bin/env python3
""" LFU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Put and get to a caching dictionary
    """
    def __init__(self):
        super().__init__()
        self._count = dict()

    def put(self, key, item):
        """ put key value pair to dict
        """
        disc_key = key
        if key is not None and item is not None:
            if self.cache_data.get(key):
                self._count[key] += 1
            else:
                if len(self._count) > 0:
                    disc_key = min(self._count, key=self._count.get)
                self._count[key] = 1
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(disc_key))
                del self.cache_data[disc_key]
                del self._count[disc_key]

    def get(self, key):
        """ return value of key
        """
        item = self.cache_data.get(key)
        if item:
            count = self._count[key] + 1
            self._count.pop(key)
            self._count[key] = count
        return item
