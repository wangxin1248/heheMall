from django.urls import path, re_path
from . import views


"""
商品模块url控制
"""
urlpatterns = [
    # 首页
    re_path(r'^$', views.index),
    # 列表页
    re_path(r'^list/(\d+)/(\d+)/(\d+)/$', views.list),
    # 商品详情页
    re_path(r'^good/(\d+)/$', views.detail)
]
