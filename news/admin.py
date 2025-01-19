"""email news letters"""
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """admin  manage news letters"""
    list_display = ('title', 'content')
    list_filter = ('title',)
    published_at = ('email',)
    ordering = ('-title',)