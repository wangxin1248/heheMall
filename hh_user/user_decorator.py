"""
用户登陆验证
http://127.0.0.1/200/?type=10
request.path():表示当前路径，为/200/
request.get_full_path():表示完整路径，为/200/?type=10
"""
from django.http import HttpResponseRedirect


# 如果未登陆则转到登陆页面
def login(func):
    def login_func(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red

    return login_func
