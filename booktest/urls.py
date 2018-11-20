from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', index),
    path('', new_index),
    re_path(r'^(\d+)$', show),
    path('upload_pic/', upload_pic),
    path('upload_handle/', upload_handle),
]
