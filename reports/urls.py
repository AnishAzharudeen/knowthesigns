from django.urls import path
from . import views

urlpatterns = [
    path("add-report-details/",
         views.add_report_details,
         name="add-report-details"),
    path("worker-login/", views.worker_login_page, name="worker-login"),
    path("worker-logout/", views.logout_user, name="worker-logout"),
    path("view-reports/", views.view_reports, name="view-reports"),
    path("report-detail/<int:report_id>/",
         views.report_detail,
         name="report-detail"),
]
