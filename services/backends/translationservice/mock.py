import requests
import json
from django.conf import settings
from requests import Response
from typing import List, Dict


class MockTranslationEngine:
    """Mock translation backend"""

    # For running tests, mock service supports only 3 locales
    possible_locale_list: List[str] = ["en", "de", "fr"]

    def translate(self, source: str, target: str, text: str) -> str:
        """mock translate method to translate hello in en, de and fr"""

        if target == "en":
            return "hello"
        if target == "de":
            return "hallo"
        if target == "fr":
            return "bonjour"
        return ""

    def validate_locale(self, locale: str) -> bool:
        """Validates if translation service supports this locale"""

        return locale in self.possible_locale_list

    def get_locales(self) -> List[str]:
        """Gets the list of supported locales"""
        return self.possible_locale_list
