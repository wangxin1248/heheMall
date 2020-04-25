from django.contrib import admin
from hh_good.models import *


# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 't_title', 'is_delete']


class GoodInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'g_title', 'g_pic', 'g_price', 'g_intro', 'g_stock', 'g_click', 'g_desc', 'g_type', 'is_delete']

# 注册模型类
admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodInfo, GoodInfoAdmin)
