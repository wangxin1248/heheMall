from django.db import models

# 购物车模型类
class CartInfo(models.Model):
    # 用户
    user = models.ForeignKey('hh_user.UserInfo', on_delete=models.CASCADE)
    # 商品
    good = models.ForeignKey('hh_good.GoodInfo', on_delete=models.CASCADE)
    # 数量
    count = models.IntegerField()
