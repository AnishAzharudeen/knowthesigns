from django.shortcuts import render


def stories(request):
    return render(request, 'stories/stories.html')