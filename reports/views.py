from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report


def create_report(request):
    '''Creates a report and returns the report details page.'''
    form = ReportForm(request.POST)
    form.save()

    return redirect('add-report-details', form.instance.id)


def add_report_details(request, report_id):
    '''Returns the add report details page.'''

    report = Report.objects.get(pk=report_id)

    context = {
        'report': report
    }
    return render(request, 'reports/add-report-details.html', context)
