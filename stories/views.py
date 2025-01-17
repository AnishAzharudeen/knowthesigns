from django.shortcuts import render
from .models import Story


def stories(request):
    '''Main page to show victim stories'''
    context = {
        'stories': Story.objects.all().order_by('-show_on_homepage')
    }
    return render(request, 'stories/stories.html', context)
