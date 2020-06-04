import datetime
from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from hh_user import user_decorator
from .models import OrderInfo, OrderDetailInfo
from hh_user.models import UserInfo
from hh_cart.models import CartInfo
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
@transaction.atomic()
@user_decorator.login
def handle(request):
    """
    订单处理功能
    :param request:post需要的数据：cart_ids、total
    :return:
    订单创建流程：
    采用事务的方式执行：一旦操作失败则全部回退
    1、创建订单对象
    2、判断商品的库存
    3、创建详单对象
    4、修改商品库存
    5、删除购物车
    """
    # 创建事务状态保存点
    tran_id = transaction.savepoint()
    try:
        # 创建订单对象
        order = OrderInfo()
        now_time = datetime.datetime.now()
        # 查询当前用户的id
        user_id = request.session.get('user_id')
        # 对订单对象的属性进行赋值
        order.order_id = '%s%d'%(now_time.strftime('%Y%m%d%H%M%S'), user_id)
        order.user_id = user_id
        order.order_date = now_time
        order.order_total = Decimal(request.POST.get('total'))
        # 保存订单对象
        order.save()
        # 查询所有的购物车信息
        carts = CartInfo.objects.filter(user_id=user_id)
        for cart in carts:
            detail = OrderDetailInfo()
            detail.order = order
            # 查询购物车信息
            cart = CartInfo.objects.get(id=cart.id)
            # 判断商品库存
            good = cart.good
            # 假如商品库存大于购买数量
            if good.g_stock >= cart.count:
                # 减少商品库存
                good.g_stock = cart.good.g_stock - cart.count
                good.save()
                # 完善订单详单信息
                detail.goods_id = good.id
                detail.price = good.g_price
                detail.count = cart.count
                # 保存订单详细信息对象
                detail.save()
                # 删除购物车对象
                cart.delete()
            else:
                # 假如库存数量小于购买数量则直接回滚
                transaction.savepoint_rollback(tran_id)
                # 重定向到购物车界面
                return redirect('/cart/')
        # 完成操作提交事务
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_id)
    # 重定向到用户的订单界面
    return redirect('/user/order/')


@user_decorator.login
def pay(request, order_id):
    """
    订单支付功能
    :param request:
    :param order_id:
    :return:
    """
    # 查询订单对象
    order = OrderInfo.objects.get(order_id=order_id)
    # TODO 完成订单支付接口调用
    # 修改订单支付状态
    order.order_is_pay = True
    # 保存订单信息
    order.save()
    context = {
        'order': order,
    }
    # 转到指定页面
    return render(request, 'hh_order/pay.html', context)
