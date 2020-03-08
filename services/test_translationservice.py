from django.test import SimpleTestCase
from typing import List
from services.translationservice import TranslationService

translation_service = TranslationService()


class TranslationServiceTest(SimpleTestCase):
    def test_translate(self):
        translated_text: str = translation_service.translate("en", "de", "hello")
        self.assertEqual(translated_text, "hallo")

    def test_get_locales(self):
        locales: List[str] = translation_service.get_locales()
        self.assertListEqual(locales, ["en", "de", "fr"])

    def test_validate_locale_true(self):
        self.assertTrue(translation_service.validate_locale("en"))

    def test_validate_locale_false(self):
        self.assertFalse(translation_service.validate_locale("hi"))
