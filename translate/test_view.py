import json
import time
from django.test import SimpleTestCase
from django.urls import reverse
from services.cachingservice import CachingService

caching_service = CachingService()


class TranslateViewTest(SimpleTestCase):

    #### Bad Request tests ####

    def test_empty_params_return_400(self):
        response = self.client.get(reverse("translate:translate"))
        self.assertEqual(response.status_code, 400)

    def test_empty_source_locale_return_400(self):
        params: str = "?target=de&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_data["error"], "source locale is empty")

    def test_empty_target_locale_return_400(self):
        params: str = "?source=en&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_data["error"], "target locale is empty")

    def test_empty_text_return_400(self):
        params: str = "?source=en&target=de"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_data["error"], "text is empty")

    def test_invalid_source_locale_return_400(self):
        params: str = "?source=test&target=de&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            response_data["error"], "Sorry, we do not support source locale - test"
        )

    def test_invalid_target_locale_return_400(self):
        params: str = "?source=en&target=test&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            response_data["error"], "Sorry, we do not support target locale - test"
        )

    #### Success response tests ####

    def test_translation_success(self):
        params: str = "?source=en&target=de&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_data["source"], "en")
        self.assertEqual(response_data["target"], "de")
        self.assertEqual(response_data["source_text"], "hello")
        self.assertEqual(response_data["translated_text"], "hallo")

    #### Caching test ####

    def test_translation_saved_in_cache(self):
        params: str = "?source=en&target=de&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 200)
        time.sleep(1)
        cached_translation = caching_service.get("en-dehello")
        self.assertEqual(cached_translation, "hallo")

    #### Pre-caching test ####

    def test_translation_precaching(self):
        params: str = "?source=en&target=de&text=hello"
        response = self.client.get(reverse("translate:translate") + params)
        self.assertEqual(response.status_code, 200)
        time.sleep(1)
        cached_translation = caching_service.get("en-frhello")
        self.assertEqual(cached_translation, "bonjour")

