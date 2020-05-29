from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from hh_user import user_decorator
from django.core.paginator import Paginator,Page

# Create your views here.
@user_decorator.login
def cart(request):
    """
    显示购物车页面
    """
    # 查询当前用户的id
    user_id = request.session.get('user_id')
    # 查询所有的购物车信息
    carts = CartInfo.objects.filter(user_id=user_id)
    # 构造页面所需的数据
    context = {
        'title':'购物车',
        'carts':carts
    }
    return render(request, 'hh_cart/cart.html', context)

@user_decorator.login
def add(request, good_id, good_count):
    """
    用户将商品加入购物车
    """
    # 查询当前用户的id
    user_id = request.session.get('user_id')
    # 用户加入的商品
    good_id = int(good_id)
    # 用户选择的数量
    good_count = int(good_count)
    # 查询购物车中是否已经有此商品，如果有则数量增加，如果没有则新增
    carts = CartInfo.objects.filter(user_id=user_id, good_id=good_id)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count+good_count
    else:
        cart = CartInfo()
        cart.user_id = user_id
        cart.good_id = good_id
        cart.count = good_count
    cart.save()
    # 获取当前购物车的总数
    count = CartInfo.objects.filter(user_id=user_id).count()
    # 将购物车的数量保存到session中
    request.session['count'] = count
    # 如果是ajax请求则返回json，否则转向购物车
    if request.is_ajax():
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

@user_decorator.login
def edit(request, cart_id, count):
    """
    修改购物车信息
    :param request:
    :param cart_id:
    :param count:
    :return:
    """
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count = int(count)
        cart.save()
        # 删除成功响应结果
        data = {'ok':0}
    except Exception as e:
        # 删除失败响应结果
        data = {'ok': count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    """
    删除购物车
    :param request:
    :param cart_id:
    :return:
    """
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        # 删除成功响应结果
        data = {'ok': 0}
    except Exception as e:
        # 删除失败响应结果
        data = {'ok': 1}
    return JsonResponse(data)