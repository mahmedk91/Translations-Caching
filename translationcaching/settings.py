import os, sys

######## DJANGO RELATED SETTINGS ########

SECRET_KEY = "2kq4h&etjsvvh86-i^!473@2g@ay&qp%hmae211c5$y%=u9q*u"

DEBUG = True

INSTALLED_APPS = ["django.contrib.auth", "django.contrib.contenttypes", "translate"]

MIDDLEWARE = ["translationcaching.middlewares.StatsMiddleware"]

ROOT_URLCONF = "translationcaching.urls"

WSGI_APPLICATION = "translationcaching.wsgi.application"

LOGGING = {
    "version": 1,
    "handlers": {"console": {"class": "logging.StreamHandler", "stream": sys.stdout,}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

#########################################

# Celery broker
CELERY_BROKER_URL = "amqp://guest:guest@localhost"

# Cache backend
CACHE_SERVICE_BACKEND = "services.backends.cachingservice.djangocache.DjangoCache"

# Django cache settings since we chose DjangoCache as our cache service backend
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
        "TIMEOUT": None,  # None means persist cache forever.
    }
}

# Translation backend
TRANSLATION_SERVICE_BACKEND = "services.backends.translationservice.yandex.Yandex"

# Yandex translation engine settings since we chose Yandex as our translation service backend
YANDEX_API_PATH = "https://translate.yandex.net/api/v1.5/tr.json/translate"
YANDEX_API_KEY = ""
