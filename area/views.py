from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *


# 省市区选择
def area_index(request):
    return render(request, 'area/area.html')


def pro(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)

    list = []
    for area in prolist:
        list.append([area.id, area.title])

    response_data = {'data': list}
    return JsonResponse(response_data)


def city(request, pro_id):
    city_list = AreaInfo.objects.filter(parea_id=pro_id)
    list = []
    for area in city_list:
        list.append({'id': area.id, 'title': area.title})

    response_data = {'data': list}
    return JsonResponse(response_data)


# 自定义编辑器
def html_editor(request):
    return render(request, 'area/editor.html')


def html_content(request):
    return HttpResponse(request.POST['hcontent'])
