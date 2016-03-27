from django.contrib import admin
from .models import News, Comments
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'adding_time']
    list_display_link = ['title']
    list_per_page = 20
    ordering = ['adding_time']
    list_filter = ['adding_time']
    search_fields = ['title', 'adding_time', 'news_content']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['commented_by', 'news_commented', 'commenting_time']
    list_per_page = 20
    ordering = ['commented_by', 'commenting_time', 'news_commented']
    search_fields = ['commented_by', 'commenting_time', 'news_commented']
    list_filter = ['commenting_time', 'commented_by', 'news_commented']

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
