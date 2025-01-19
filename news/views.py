from django.shortcuts import render, HttpResponse
import requests
import os
from django.core.paginator import Paginator

if os.path.isfile("env.py"):
    import env

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

def get_news(request):
    # URL de la API de noticias
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "child labor OR Slavery Prevention OR Modern Slavery",
        "from": "2015-01-01",
        "language": "en",
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY,
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            # Extraer noticias de la respuesta JSON
            news_data = response.json()
            articles = news_data.get("articles", [])
            
           # Filtrar noticias válidas
            valid_articles = [
                article for article in articles 
                if article.get("title") != "[Removed]"
                and article.get("description") != "[Removed]"
                and article.get("content") != "[Removed]"
                and article.get("urlToImage")  # Verifica que urlToImage no esté vacío o sea None
            ][:30]  # Máximo 16 noticias válidas

        else:
            valid_articles = []

    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        valid_articles = []

    # Implementar la paginación
    paginator = Paginator(valid_articles, 12)  # 4 noticias por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "news.html", {"page_obj": page_obj})
