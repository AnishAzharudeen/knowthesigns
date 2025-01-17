from django.db import models


class Report(models.Model):
    '''Model for creating a report that contains the user's message.'''
    message = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    actioned = models.BooleanField(default=False)
    actioned_date = models.DateTimeField(null=True)


class ReportDetails(models.Model):
    '''Model for report details to be added to a report.'''
    name = models.CharField(max_length=50, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
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
