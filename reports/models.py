from django.db import models


class Report(models.Model):
    message = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    actioned = models.BooleanField(default=False)
    actioned_date = models.DateTimeField(null=True)
