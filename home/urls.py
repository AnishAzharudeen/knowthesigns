from . import views
from reports.views import create_report
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("create-report", create_report, name="create-report"),
]
