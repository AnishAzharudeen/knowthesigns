'''Admin panels for stories app.'''
from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    '''
    Creates panel for admins to create, view, update and delete stories.
    '''

    list_display = ('title', 'content', 'date_created')