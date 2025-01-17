'''Contains the forms for the reports app.'''
from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    '''Form for creating a report'''
    class Meta:
        model = Report
        fields = ['message']