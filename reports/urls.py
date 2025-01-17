from django.urls import path
from . import views

urlpatterns = [
    path("add-report-details/<int:report_id>",
         views.add_report_details,
         name="add-report-details"),
]
