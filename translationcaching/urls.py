from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path("translate", include("translate.urls")),  # include urls from translate app
]
