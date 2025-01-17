'''Contains the forms for the reports app.'''
from django import forms
from .models import Report, ReportDetails


class ReportForm(forms.ModelForm):
    '''Form for creating a report'''
    class Meta:
        model = Report
        fields = ['message']


class ReportDetailsForm(forms.ModelForm):
    '''Form for adding details to a report'''
    class Meta:
        model = ReportDetails
        # Include all fields on model apart from report and image/vid URL
        exclude = ['report', 'image_video_url']
