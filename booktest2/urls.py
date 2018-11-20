from django.urls import path, re_path
from .views import *

app_name = 'booktest'

urlpatterns = [
    path('', index, name='index'),
    # re_path("^(\d+)$", detail, name='detail'),
    re_path("^(\d+)$", show, name='show'),
    path("get_test1/", get_test1),
    path("get_test2/", get_test2),
    path("get_test3/", get_test3),
    path("post_test1/", post_test1),
    path("post_test2/", post_test2),
    path("cookie_test/", cookie_test),
    path("red_test1/", red_test1),
    path("red_test2/", red_test2),
    path("session1/", session1),
    path("session2/", session2),
    path("session2_handle/", session2_handle),
    path("session3/", session3),
    path("template_test/", template_test),
    re_path("^show_hero_detail_(\d+)$", show_hero_detail, name='show_hero_detail'),
    path("child_index/", child_index),
    re_path("^user_(\d+)$", user, name='user'),
    path("html_test/", html_test),
    re_path("^csrf_(\d+)$", csrf_test, name='csrf_test'),
    re_path("^hero_list/(\d*)/?$", hero_list),
    path("cache1/", cache1),
]
