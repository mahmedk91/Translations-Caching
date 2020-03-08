import logging
from django.views import View
from translationcaching.utils import HttpResponseBadRequest, TranslationResponse
from services.translationservice import TranslationService
from services.cachingservice import CachingService
from translate.tasks import precache_translation

translation_service = TranslationService()
caching_service = CachingService()


class Translate(View):
    def get(self, request):

        # Validate source locale
        source = request.GET.get("source")
        if not source:
            return HttpResponseBadRequest("source locale is empty")
        if not translation_service.validate_locale(source):
            return HttpResponseBadRequest(
                "Sorry, we do not support source locale - {}".format(source)
            )

        # Validate target locale
        target = request.GET.get("target")
        if not target:
            return HttpResponseBadRequest("target locale is empty")
        if not translation_service.validate_locale(target):
            return HttpResponseBadRequest(
                "Sorry, we do not support target locale - {}".format(target)
            )

        # validate source text
        source_text = request.GET.get("text")
        if not source_text:
            return HttpResponseBadRequest("text is empty")

        # Try to fetch the translation first from cache
        cached_translation = caching_service.get(source + "-" + target + source_text)
        if cached_translation:
            logging.info("Translation found in cache!")
            return TranslationResponse(source, target, source_text, cached_translation)

        # If not found in cache, fetch the translation from translation engine
        logging.info("Fetching translation from translation engine")
        translated_text = translation_service.translate(source, target, source_text)

        # Add asynchronous tasks to fetch the translation for all languages
        # and save in cache
        for locale in translation_service.get_locales():
            precache_translation.delay(source, locale, source_text)

        # Return the translated text
        return TranslationResponse(source, target, source_text, translated_text)
