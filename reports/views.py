from django.shortcuts import render, redirect
from .forms import ReportForm, ReportDetailsForm
from .models import Report
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        messages.error(request, 'You have not created a report.')
        return redirect('create-full-report')

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


def create_full_report(request):
    '''Returns page to create a report and create report details.'''
    if request.method == 'POST':
        form = ReportForm(request.POST)
        form_details = ReportDetailsForm(request.POST)
        if form.is_valid() and form_details.is_valid():
            form.save()
            form_details.instance.report = form.instance
            form_details.save()

            messages.success(request, 'Report created successfully.')
            return redirect('home')

    context = {
        'report_message_form': ReportForm,
        'report_details_form': ReportDetailsForm,
    }

    return render(request, 'reports/create-full-report.html', context)


# Worker views


def worker_login_page(request):
    '''Returns the page for workers to login.'''

    # If worker already logged in, redirect to view reports page.
    if request.user.is_authenticated:
        return redirect('view-reports')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('view-reports')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'reports/workers/worker-login.html')


@login_required
def view_reports(request):
    '''Returns the page for workers to view reports.'''
    # Actioned at bottom, then oldest at bottom, then unread
    reports = Report.objects.all().order_by('actioned',
                                            'date_created',
                                            '-read')

    context = {
        'reports': reports,
    }
    return render(request, 'reports/workers/view-reports.html', context)


@login_required
def report_detail(request, report_id):
    '''Returns the page for workers to view a specific report and update it.'''
    report = Report.objects.get(pk=report_id)

    if request.method == 'POST':
        update_message = request.POST['update-message']

        # Create an action message for the report
        report.action_messages.create(worker_user=request.user,
                                      update_message=update_message)

    context = {
        'report': report
    }

    if report.read is True:
        action_messages = report.action_messages.all()

        # Add action messages to the context
        context['action_messages'] = action_messages
    else:
        report.read = True
        report.save()

    return render(request, 'reports/workers/report-detail.html', context)


@login_required
def logout_user(request):
    '''Logs out the worker and redirects to the home page.'''
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')


@login_required
def mark_report_resolved(request, report_id):
    '''
        Marks a report as resolved when 'Mark as (un)resolved' tbn is clicked.
        Uses AJAX to update the report actioned boolean.
    '''
    if request.method == 'POST':
        report = Report.objects.get(pk=report_id)
        report.actioned = not report.actioned
        report.save()
        response_data = {'message': 'success'}
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
