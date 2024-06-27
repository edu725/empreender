from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('add/', add_item, name='add_item'),
    path('edit/<int:item_id>/', edit_item, name='edit_item'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]