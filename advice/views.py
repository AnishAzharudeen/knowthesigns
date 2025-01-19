from django.shortcuts import render


def advice(request):
    """
    A view to show the advice page
    """

    return render(request, "advice/advice.html")
