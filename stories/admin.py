'''Admin panels for stories app.'''
from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    '''
    Creates panel for admins to create, view, update and delete stories.
    '''

    list_display = ('title', 'content', 'date_created')
    actions = ['add_to_homepage', 'remove_from_homepage']

    def add_to_homepage(self, queryset):
        '''Action to add selected story to the homepage stories section'''
        queryset.update(show_on_homepage=True)

    def remove_from_homepage(self, queryset):
        '''Action to remove selected story from the homepage stories section'''
        queryset.update(show_on_homepage=False)
