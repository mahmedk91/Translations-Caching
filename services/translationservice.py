from services.backends.translationservice.yandex import Yandex
from typing import List
from django.utils.module_loading import import_module
from django.conf import settings


class TranslationService:
    """A wrapped translation service which requires a backend to work"""

    def __init__(self):
        # Get the backend as configued in django settings
        BackendClass = self.get_backend()
        self.backend = BackendClass()

    def translate(self, source: str, target: str, text: str) -> str:
        """Translate the given text from source locale to target"""

        return self.backend.translate(source, target, text)

    def validate_locale(self, locale: str) -> bool:
        """Validates if translation service supports this locale"""

        return self.backend.validate_locale(locale)

    def get_locales(self) -> List[str]:
        """Gets the list of supported locales"""

        return self.backend.get_locales()

    def get_backend(self):
        """Injects the backend as configured in django settings"""

        if not settings.TRANSLATION_SERVICE_BACKEND:
            raise Exception("TRANSLATION_SERVICE_BACKEND is not provided")

        package, klass = settings.TRANSLATION_SERVICE_BACKEND.rsplit(".", 1)

        module = import_module(package)

        return getattr(module, klass)
