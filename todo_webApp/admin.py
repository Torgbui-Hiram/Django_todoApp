from django.contrib import admin
from . models import List, Message, Room


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('item', 'completed')
    list_filter = ('item',)
    search_fields = ('item',)


@admin.register(Room)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'room_name',)
    list_filter = ('user_name', 'room_name',)
    search_fields = ('user_name', 'room_name',)


@admin.register(Message)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('value', 'date', 'room', 'user')
    list_filter = ('value', 'date', 'room', 'user')
    search_fields = ('value', 'date', 'room', 'user')
