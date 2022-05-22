from django.urls import path, re_path
from .views import index, contacts, get_regions, find_by_name, edit_region

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('regions/', get_regions),
    path('regions/edit/', edit_region),
    path('regions/<int:id>', get_regions),
    path('regions/<slug:text>', find_by_name),
    re_path('regions/$', find_by_name),
]
