import os

######## DJANGO RELATED SETTINGS ########

SECRET_KEY = "2kq4h&etjsvvh86-i^!473@2g@ay&qp%hmae211c5$y%=u9q*u"

ROOT_URLCONF = "translationcaching.urls"

WSGI_APPLICATION = "translationcaching.wsgi.application"

INSTALLED_APPS = ["django.contrib.auth", "django.contrib.contenttypes", "translate"]

#########################################

# Celery broker
CELERY_BROKER_URL = "amqp://guest:guest@localhost"

# Mock cache backend
CACHE_SERVICE_BACKEND = "services.backends.cachingservice.mock.MockCache"

# Mock translation backend
TRANSLATION_SERVICE_BACKEND = (
    "services.backends.translationservice.mock.MockTranslationEngine"
)

