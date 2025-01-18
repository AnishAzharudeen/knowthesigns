from django.shortcuts import render
from reports.forms import ReportForm


def home(request):
    '''Home page view'''
    context = {
        'report_form': ReportForm
    }
    return render(request, 'home/index.html', context)
