from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django_test import settings
import os


def index(request):
    book_list = BookInfo.objects.all()
    context = {'list': book_list}
    return render(request, 'booktest/index.html', context)


def show(request, book_id):
    book_info = BookInfo.objects.get(pk=book_id)

    hero_list = book_info.heroinfo_set.all()
    context = {'list': hero_list}
    return render(request, 'booktest/show.html', context)


def new_index(request):
    return render(request, 'booktest/new_index.html')


def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    f1 = request.FILES['pic']
    fname = os.path.join(settings.MEDIA_ROOT, f1.name)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s">' % f1.name)
