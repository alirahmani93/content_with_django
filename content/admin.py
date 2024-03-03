from django.contrib import admin

from content.models import ContentScore
from content.models.content import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']


class ContentScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'score', 'is_active', 'created_at', 'updated_at']
    list_filter = ['score', 'is_active', 'created_at', 'updated_at']


admin.site.register(Content, ContentAdmin)
admin.site.register(ContentScore, ContentScoreAdmin)
