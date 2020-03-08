from django.test import SimpleTestCase
from services.cachingservice import CachingService

caching_service = CachingService()


class CacheServiceTest(SimpleTestCase):
    def test_cache(self):
        caching_service.set("test-key", "test-value")
        value: str = caching_service.get("test-key")
        self.assertEqual(value, "test-value")

    def test_hyphenate(self):
        value: str = caching_service.hyphenate("test value")
        self.assertEqual(value, "test-value")
