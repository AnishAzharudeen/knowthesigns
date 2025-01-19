from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator


def get_news(request):
    # Obtener todas las noticias
    all_news = News.objects.all().order_by('-published_at')

    # Implementar paginación
    paginator = Paginator(all_news, 12)  # 12 noticias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'page_obj': page_obj})
