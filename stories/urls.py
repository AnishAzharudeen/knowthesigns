from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.stories, name="stories"),
    path("advice/", views.advice, name="advice"),
]
