from django.shortcuts import render
from reports.forms import ReportForm
from stories.models import Story
from news.models import News


def home(request):
    """Home page view"""
    homepage_stories = Story.objects.filter(show_on_homepage=True)
    latest_news = News.objects.all().order_by('-published_at')[:3]  # Obtener las 3 noticias más recientes

    context = {"report_form": ReportForm, 
               "homepage_stories": homepage_stories,
               "latest_news": latest_news,}
    
    return render(request, "home/index.html", context)
