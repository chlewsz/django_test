from django.contrib import admin
from .models import *


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    # 列表页显示效果
    list_display = ['pk', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    # 修改添加页属性
    # fields = ['bpub_date', 'btitle']
    fieldsets = [
        ('base', {"fields": ['btitle']}),
        ('super', {"fields": ['bpub_date']}),
    ]

    # 嵌入关联类
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
