"""heheMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户模块相关界面的url
    re_path(r'^user/', include('hh_user.urls')),
    # 商品模块相关界面的url
    re_path(r'^', include('hh_good.urls')),
    # 购物车模块相关界面的url
    re_path(r'^cart/', include('hh_cart.urls')),
    # 订单模块相关界面的url
    re_path(r'^order/$', include('hh_order.urls')),
    # 富文本编辑器
    re_path(r'^/static/tinymce/', include('tinymce.urls')),
]
