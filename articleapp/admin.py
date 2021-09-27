from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["writer", "project", "title", "content", "created_at"]
