from .views import get_news
from django.urls import path

urlpatterns = [
    path("", get_news, name="news"),
]
