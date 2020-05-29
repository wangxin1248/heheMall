from django.urls import path, re_path
from . import views


"""
购物车模块url控制
"""
urlpatterns = [
    # 购物车页面
    re_path(r'^$', views.cart),
    # 加入购物车链接
    re_path(r'^add/(\d+)/(\d+)/$', views.add),
    # 修改购物车
    re_path(r'^edit/(\d+)_(\d+)/$', views.edit),
    # 删除购物车
    re_path(r'^delete/(\d+)/$', views.delete),
]
