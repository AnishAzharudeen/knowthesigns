from django.shortcuts import render, HttpResponse
import requests
import os


if os.path.isfile("env.py"):
    import env

NEWS_API_KEY = os.environ.get("NEWS_API_KEY"),

def getAPI(request):
    # URL de productos
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "tesla",
        "from": "2024-12-19",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
            news = response.json()
            """
            for producto in productos:
                print(producto)
            """
            return HttpResponse(news) or []
        
    except request.RequestException as e:
        print("Error en la solicitud: (e)")
        news = []
    
    return render(request, 'news.html', {'productos': news})


