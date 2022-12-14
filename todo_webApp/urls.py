from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/<id>', views.show_item, name='show'),
    path('search', views.shearch_item, name='search'),
    path('delete/<id>', views.delete_item, name='delete'),
    path('cross_off/<id>', views.cross_off, name='crossoff'),
    path('uncross/<id>', views.uncross, name='uncross'),
    path('edit_item/<id>', views.edit_item, name='edit'),
    path('add_item', views.add_item, name='add'),
]
