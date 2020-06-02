from django.db import models

# 订单模块对应的模型类


class OrderInfo(models.Model):
    """
    订单信息主类
    """
    # 订单id
    order_id = models.CharField(max_length=20, primary_key=True)
    # 订单用户
    user = models.ForeignKey('hh_user.UserInfo', on_delete=models.CASCADE)
    # 订单时间
    order_date = models.DateTimeField(auto_now=True)
    # 订单支付状态
    order_is_pay = models.BooleanField(default=False)
    # 订单总金额
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    # 订单地址
    order_address = models.CharField(max_length=100)
    # TODO 真实支付
    # TODO 物流信息


class OrderDetailInfo(models.Model):
    """
    订单详情类
    """
    # 订单中的商品
    goods = models.ForeignKey('hh_good.GoodInfo', on_delete=models.CASCADE)
    # 所属订单
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    # 订单中商品的价格
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 订单中的商品数量
    count = models.IntegerField()

