from django.contrib import admin
from . models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('item', 'completed')
    list_filter = ('item',)
    search_fields = ('item',)
