from django.core.cache import cache


class DjangoCache:
    """Django cache backend"""

    def set(self, key: str, value):
        """Sets a key value in cache"""

        cache.set(key, value)

    def get(self, key: str):
        """Gets a key value from cache"""

        return cache.get(key)
