from django.urls import path, re_path
from .views import *


app_name = 'area'

urlpatterns = [
    path('', area_index, name='area_index'),
    path('pro/', pro, name='area_pro_list'),
    re_path(r'^city_(\d+)/', city, name='area_city_list'),
    path('html_editor/', html_editor),
    path('html_content/', html_content),
]
