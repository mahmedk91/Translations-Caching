import shelve


class MockCache:
    """Mock cache backend - uses python shelve for mocking cache - https://docs.python.org/3/library/shelve.html"""

    def set(self, key: str, value):
        """Sets a key value in cache"""

        with shelve.open("test_cache.dat") as cache:
            cache[key] = value

    def get(self, key: str):
        """Gets a key value from cache"""

        with shelve.open("test_cache.dat") as cache:
            return cache.get(key)
