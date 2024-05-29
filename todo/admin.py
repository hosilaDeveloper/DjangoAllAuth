from django.contrib import admin
from .models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    list_display_links = ('id', 'title', 'completed')
    search_fields = ('title', 'completed')
    list_filter = ('completed', 'title')

