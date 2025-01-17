'''Models for the stories app'''
from django.db import models


class Story(models.Model):
    '''Model for a story'''
    title = models.CharField(max_length=15, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''String representation of a story'''
        return str(self.title)
