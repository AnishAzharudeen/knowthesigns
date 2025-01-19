from django.shortcuts import render
from reports.forms import ReportForm
from stories.models import Story


def home(request):
    """Home page view"""
    homepage_stories = Story.objects.filter(show_on_homepage=True)
    context = {"report_form": ReportForm, "homepage_stories": homepage_stories}
    return render(request, "home/index.html", context)
