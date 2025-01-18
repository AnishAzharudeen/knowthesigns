from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    '''Model for creating a report that contains the user's message.'''
    message = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    actioned = models.BooleanField(default=False)
    actioned_date = models.DateTimeField(null=True)


class ReportDetails(models.Model):
    '''Model for report details to be added to a report.'''
    report = models.OneToOneField(Report, related_name="details",
                                  on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    first_line_address = models.CharField(max_length=100,
                                          null=True,
                                          blank=True)
    second_line_address = models.CharField(max_length=100,
                                           null=True,
                                           blank=True)
    town_city = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    person_of_trust = models.CharField(max_length=50, null=True, blank=True)
    person_of_trust_phone_number = models.CharField(max_length=15,
                                                    null=True,
                                                    blank=True)
    image_video_url = models.URLField(null=True, blank=True)


class ActionMessage(models.Model):
    '''Model for action messages to be added to a report by workers.'''
    report = models.ForeignKey(Report, related_name="action_messages",
                               on_delete=models.CASCADE)
    worker_user = models.ForeignKey(User, on_delete=models.CASCADE)
    update_message = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
