from django.shortcuts import render, redirect
from .forms import ReportForm, ReportDetailsForm
from .models import Report
from django.contrib import messages
from django.http import HttpResponseForbidden


def create_report(request):
    '''Creates a report and returns the report details page.'''
    form = ReportForm(request.POST)
    form.save()

    # Saves the report ID in the session to be used in the next view
    request.session['report_id'] = form.instance.id

    messages.success(request, 'Report created successfully.')

    return redirect('add-report-details')


def add_report_details(request):
    '''Returns the add report details page.'''

    # Retrieves report id from session that was added upon report creation
    report_id = request.session.get('report_id')

    # If user got here without creating a report, return a forbidden response
    if not report_id:
        return HttpResponseForbidden('You have not created a report.')

    report = Report.objects.get(pk=report_id)

    if request.method == 'POST':
        form = ReportDetailsForm(request.POST)
        if form.is_valid():
            form.instance.report = report
            form.save()
            messages.success(request,
                             'Report details added to report successfully.')
            return redirect('home')

    context = {
        'report': report,
        'report_details_form': ReportDetailsForm,
    }
    return render(request, 'reports/add-report-details.html', context)
