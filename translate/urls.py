from django.urls import path
from translate.views import Translate

app_name = "translate"
urlpatterns = [path("", Translate.as_view(), name="translate")]
