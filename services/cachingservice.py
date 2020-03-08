from django.utils.module_loading import import_module
from django.conf import settings


class CachingService:
    """A wrapped caching service which requires a backend to work"""

    def __init__(self):
        # Get the backend as configued in django settings
        BackendClass = self.get_backend()
        self.backend = BackendClass()

    def hyphenate(self, key: str) -> str:
        """Replaces the empty spaces in a key with hyphens"""

        return "-".join(key.split())

    def set(self, key: str, value):
        """Sets a key value in cache"""

        hyphenated_key = self.hyphenate(key)
        self.backend.set(hyphenated_key, value)

    def get(self, key: str):
        """Gets a key value from cache"""

        hyphenated_key = self.hyphenate(key)
        return self.backend.get(hyphenated_key)

    def get_backend(self):
        """Injects the backend as configured in django settings"""

        if not settings.CACHE_SERVICE_BACKEND:
            raise Exception("CACHE_SERVICE_BACKEND is not provided")

        package, klass = settings.CACHE_SERVICE_BACKEND.rsplit(".", 1)

        module = import_module(package)

        return getattr(module, klass)
