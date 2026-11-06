from django.contrib import admin

from .models import HealthArticle


@admin.register(HealthArticle)
class HealthArticleAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'published_date']
  list_filter = ['category']
  search_fields = ['title', 'summary', 'content']
