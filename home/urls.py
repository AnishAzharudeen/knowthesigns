from . import views
from reports.views import create_report
from django.urls import path

urlpatterns = [
    path("", views.home, name="homepage"),
    path("create-report", create_report, name="create-report"),
]
