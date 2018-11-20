from django.shortcuts import render, redirect
from .models import *
from django.db.models import Max, F, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')  # 内联查询
    # list = BookInfo.books1.filter(pk__lt=3)  # 主键小于3的

    # 使用F对象来比较两列，同时F对象支持运算
    # list = BookInfo.books1.filter(bread__gt=F('bcomment'))

    # 使用Q对象来实现逻辑或
    # list = BookInfo.books1.filter(Q(pk__lt=4) | Q(btitle__contains="1"))

    max_date = BookInfo.books1.aggregate(Max('bpub_date'))  # 聚合

    context = {
        "list1": list,
        "max_date": max_date
    }
    return render(request, 'booktest2/index.html', context)


def detail(request, pi):
    return HttpResponse(pi)


# 展示链接的页面
def get_test1(request):
    return render(request, 'booktest2/getTest1.html')


# 展示一键一值的情况
def get_test2(request):
    # 根据键接收值
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    # 构造上下文
    context = {'a': a, 'b': b, 'c': c}

    # 向模板中传递上下文，并进行渲染
    return render(request, 'booktest2/getTest2.html', context)


# 展示一键多值的情况
def get_test3(request):
    a = request.GET.getlist('a')
    context = {'a': a}
    return render(request, 'booktest2/getTest3.html', context)


def post_test1(request):
    return render(request, 'booktest2/postTest1.html')


def post_test2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'name': uname, 'pwd': upwd, 'gender': ugender, 'hobby': uhobby}
    return render(request, 'booktest2/postTest2.html', context)


# 注意：跨域名无法共享cookie信息
def cookie_test(request):
    response = HttpResponse()
    cookies = request.COOKIES
    if cookies['t1']:
        response.write(cookies['t1'])
    # response.set_cookie('t1', 'abc')
    return response


def red_test1(request):
    # return HttpResponseRedirect('/booktest/red_test2/')
    return redirect('/booktest/red_test2/')


def red_test2(request):
    return HttpResponse('这是重定向来的页面')


# 通过用户登录练习session
def session1(request):
    name = request.session.get("myname", '未登录')
    context = {"name": name}
    return render(request, 'booktest2/session1.html', context)


def session2(request):
    return render(request, 'booktest2/session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0)  # 设置session失效时间，为0则浏览器关闭就失效
    return redirect('/booktest/session1/')


def session3(request):
    if 'myname' in request.session.keys():
        del request.session['myname']
    # request.session.flush()  # 清空session和cookie
    return redirect('/booktest/session1/')


def template_test(request):
    # hero = HeroInfo.objects.get(pk=1)
    # context = {'hero': hero}

    list = HeroInfo.objects.all()
    context = {'list': list}
    return render(request, 'booktest2/template_test.html', context)


def show(request, id):
    context = {'id': id}
    return render(request, 'booktest2/show.html', context)


def show_hero_detail(request, hero_id):
    hero = HeroInfo.objects.get(pk=hero_id)
    context = {'hero': hero}
    return render(request, 'booktest2/show_hero_detail.html', context)


def child_index(request):
    return render(request, 'booktest2/child_index.html')


def user(request, index):
    if '1' == index:
        return render(request, 'booktest2/user_first.html')
    elif '2' == index:
        return render(request, 'booktest2/user_second.html')
    else:
        return HttpResponse('什么都没有匹配')


# html转移
def html_test(request):
    context = {'t1': '<h1>t1</h1>'}
    return render(request, 'booktest2/html_test.html', context)


# csrf
def csrf_test(request, index):
    if '1' == index:
        return render(request, 'booktest2/csrf1.html')
    elif '2' == index:
        name = request.POST['name']
        context = {'name': name}
        return render(request, 'booktest2/csrf2.html', context)
    else:
        return HttpResponse('路径错误')


def hero_list(request, pindex):
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest2/hero_list.html', context)


# 缓存视图
@cache_page(60)
def cache1(request):
    print("使用cache")
    return HttpResponse('hello1')


# 缓存模板
def cache2(request):
    print("使用cache")
    return render(request, 'booktest2/cache2.html')


# 自定义缓存数据
def cache3(requst):
    # cache.set('key1', 'value1', 600)
    # print(cache.get('key1'))
    cache.clear()  # 清空缓存
    return render(requst, 'booktest2/cache2.html')
