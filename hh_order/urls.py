from django.urls import path, re_path
from . import views


"""
订单模块url控制
"""
urlpatterns = [
    # 首页
    re_path(r'^$', views.index),
]
