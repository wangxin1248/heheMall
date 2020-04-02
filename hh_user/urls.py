from django.urls import path, re_path
from . import views

urlpatterns = [
    # 登陆页面请求
    re_path(r'^login/$', views.login),
    # 注册页面请求
    re_path(r'^register/$', views.register),
    # 用户信息页面请求
    re_path(r'^info/$', views.user_info),
    # 用户订单信息页面请求
    re_path(r'^order/$', views.user_order),
    # 用户中心页面请求
    re_path(r'^site/$', views.user_site),
    # 注册请求处理
    re_path(r'^register_handle/$', views.register_handle),
    # 登陆请求处理
    re_path(r'^login_handle/$', views.login_handle),
    # 查询用户是否存在
    re_path(r'^register_exits/$', views.register_exits),
    # 用户中心修改用户的个人信息
    re_path(r'^save_user_info/$', views.save_user_info),
]