from django.db import models
from tinymce.models import HTMLField


# 商品类别
class TypeInfo(models.Model):
    # 类别名称
    t_title = models.CharField(max_length=20)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.t_title)


# 商品
class GoodInfo(models.Model):
    # 商品名称
    g_title = models.CharField(max_length=20)
    # 商品图片
    g_pic = models.ImageField(upload_to='hh_good')
    # 商品价格
    g_price = models.DecimalField(max_digits=5, decimal_places=2)
    # 商品简介
    g_intro = models.CharField(max_length=200)
    # 商品库存
    g_stock = models.IntegerField()
    # 商品点击量
    g_click = models.IntegerField(default=0)
    # 商品描述
    g_desc = HTMLField()
    # 商品所属类别（外键）
    g_type = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.g_title)
