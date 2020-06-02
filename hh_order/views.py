from django.shortcuts import render
from django.db import transaction
from hh_user import user_decorator
from hh_user.models import UserInfo
from hh_cart.models import CartInfo

# Create your views here.


@user_decorator.login
def index(request):
    """
    订单首页
    :param request:
    :return:
    """
    # 查询当前用户的id
    user_id = request.session.get('user_id')
    # 查询用户对象，使用主键查询，得用 get，使用字段查询的话得使用字段名
    user = UserInfo.objects.get(id=user_id)
    # 查询用户对应的详细地址
    addr = user.u_addr
    if addr == '':
        addr = '无详细地址'
    name = user.u_real_name
    if name == '':
        name = '新用户'
    phone = user.u_phone
    if phone == '':
        phone = '无手机信息'
    user_addr = addr+' ('+name+' 收)'+' '+phone
    # 查询所有的购物车信息
    carts = CartInfo.objects.filter(user_id=user_id)
    # 构造页面所需的数据
    context = {
        'title': '提交订单',
        'addr': user_addr,
        'carts': carts
    }
    return render(request, 'hh_order/order.html', context)


@user_decorator.login
def order(request, cart_id):
    """
    订单处理功能
    :param request:
    :param cart_id:
    :return:
    订单创建流程：
    采用事务的方式执行：一旦操作失败则全部回退
    1、创建订单对象
    2、判断商品的库存
    3、创建详单对象
    4、修改商品库存
    5、删除购物车
    """
    return render(request, 'hh_order/order.html')
