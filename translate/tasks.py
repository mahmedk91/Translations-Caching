from celery import shared_task

from services.translationservice import TranslationService
from services.cachingservice import CachingService

translation_service = TranslationService()
caching_service = CachingService()


@shared_task
def precache_translation(source: str, target: str, text: str):
    # Fetch translation from translation service
    translated_text = translation_service.translate(source, target, text)

    # Save translation in cache
    print("Saving translation for locale {0} in cache!".format(target))
    caching_service.set(source + "-" + target + text, translated_text)
