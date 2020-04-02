from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """
    用户信息
    """
    # 用户名
    u_name = models.CharField(max_length=10)
    # 用户密码
    u_pwd = models.CharField(max_length=40)
    # 用户手机
    u_phone = models.CharField(max_length=11)
    # 用户邮箱
    u_email = models.CharField(max_length=30, default='')
    # 真实姓名
    u_real_name = models.CharField(max_length=10, default='')
    # 地址
    u_addr = models.CharField(max_length=100, default='')
    # 邮编
    u_code = models.CharField(max_length=6, default='')


