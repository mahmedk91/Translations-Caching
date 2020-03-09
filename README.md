# Translation Caching

A Django app for translation API with pluggable translation engine and caching mechanism.

## Design Architecture

### Cache

Django app already comes up with alot of plugins - including cache. Since we want to be flexible, we have wrapped django cache in a service. The service always require a backend to work which must be injected when the app starts.

We have made our django cache permanently persistant. However, this can be changed by changing the `TIMEOUT` value in django settings.

In order, to use any other caching service - one just require to write a new backend and configure in django settings. One example of such is `MockCache` backend which is used in tests.

### Translation

There are several translation engines out there - Google, Bing, Yandex. We used Yandex as our translation engine as its free and easy to use.

Translation service (just like cache) requires a backend. One can easily write another backend for using another translation engine without changing any code.

### Pre-caching

Pre-caching needs to be asynchronous to keep the translation API fast. We needed a message broker and a service to publish-subscribe messages. We use Celery with RabbitMQ broker. Celery has inbuild support for Django and comes preconfigured with 4 workers.

### Stats middleware

We needed to measure improvement in the response time when the translation is cached. Thankfully, with Django we can write custom middleware to do something before and after the response. We wrote a stats middleware which logs the time elapsed for processing the request. It makes it easy to measure request time and see the advantage to caching and pre-caching in our architecture.

## Setup

### Tools needed

- Python3 and pip
- virtualenv running Python3
- running RabbitMQ server - https://www.rabbitmq.com/download.html

### Installation

`virtualenv -p python3 venv_translation_caching`

`source venv_translation_caching/bin/activate`

`pip install -r requirements.txt`

## Running the project

Start the rabbitMQ server

`export PATH=$PATH:/usr/local/opt/rabbitmq/sbin`

`rabbitmq-server`

Start the celery service to process asynchronous tasks

`DJANGO_SETTINGS_MODULE=translationcaching.settings celery -A translationcaching worker -l info`

Start the Django server

`python manage.py runserver`

Checkout the translation API

GET http://localhost:8000/translate?source=en&target=fr&text=hello

## Running tests

Start the rabbitMQ server

`export PATH=$PATH:/usr/local/opt/rabbitmq/sbin`

`rabbitmq-server`

Start the celery service to process test asynchronous tasks

`DJANGO_SETTINGS_MODULE=translationcaching.testsettings celery -A translationcaching worker -l info`

Start the Django server

`python manage.py test --settings=translationcaching.testsettings`

## Further improvments

- Translation service could be improved to fetch the list of supported locales instead of hard-coding supported locales
- Pre-fetching could be improved to prefetch translations more smartly. Currently, we prefetch translation in all languages. A user who translates from english to German, perhaps would not be interested in Chinese translation too.
- Translation API could be improved by making the `source` optional. Many translation engines also provides API to guess the text source language instead of explicitly providing the source language
