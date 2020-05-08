from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import *
from hashlib import sha1
from . import user_decorator


# 登陆界面请求
def login(request):
    """
    登陆界面请求
    测试账号：test0001
    测试密码：test0001
    """
    u_name = request.COOKIES.get('uname', '')
    context = {'tittle': '用户登陆', 'erroe_name': 0, 'error_pwd': 0, 'uname': u_name}
    return render(request, 'hh_user/login.html', context)


# 注册页面请求
def register(request):
    """
    注册页面请求
    """
    context = {'tittle': '用户注册'}
    return render(request, 'hh_user/register.html', context)


# 请求用户信息页面
@user_decorator.login
def user_info(request):
    """
    请求用户信息页面
    """
    # 判断是否保存了用户的 session 信息
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    # 如果用户没有登陆则直接跳转到登陆界面
    if user_name == '':
        return redirect('/user/login/')
    # 查询当前用户的个人信息
    user = UserInfo.objects.get(id=user_id)
    user_real_name = user.u_real_name
    user_phone = user.u_phone
    if user_phone == '':
        user_phone = '无'
    user_email = user.u_email
    if user_email == '':
        user_email = '无'
    # 构造界面显示信息
    context = {'tittle': '用户信息', 'user_name': user_real_name, 'user_phone': user_phone, 'user_email': user_email}
    return render(request, 'hh_user/user_center_info.html', context)


# 用户订单信息页面
@user_decorator.login
def user_order(request):
    """
    用户订单信息页面
    """
    # 判断是否保存了用户的 session 信息
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    # 如果用户没有登陆则直接跳转到登陆界面
    if user_name == '':
        return redirect('/user/login/')
    context = {'tittle': '订单信息'}
    return render(request, 'hh_user/user_center_order.html', context)


# 用户中心信息界面
@user_decorator.login
def user_site(request):
    """
    用户中心信息界面
    """
    # 判断是否保存了用户的 session 信息
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    # 如果用户没有登陆则直接跳转到登陆界面
    if user_name == '':
        return redirect('/user/login/')
    # 获取用户信息
    user = UserInfo.objects.get(id=user_id)
    addr = user.u_addr
    if addr == '':
        addr = '无详细地址'
    name = user.u_real_name
    if name == '':
        name = '新用户'
    phone = user.u_phone
    if phone == '':
        phone = '无手机信息'
    code = user.u_code
    if code == '':
        code = '无邮政编码'
    user_addr = addr+' ('+name+' 收)'+' '+phone
    # 构建返回用户中心页面的数据
    context = {'tittle': '用户中心',
               'user_addr': user_addr,
               'name': name,
               'phone': phone,
               'code': code,
               'addr': addr}
    return render(request, 'hh_user/user_center_site.html', context)


# 注册请求处理
def register_handle(request):
    """
    注册请求处理
    """
    # 接收用户输入
    post = request.POST
    # 确认是否输入了信息
    if len(post) == 0:
        return redirect('/user/register/')
    u_name = post['user_name']
    u_pwd = post['pwd']
    u_pwd1 = post['cpwd']
    u_email = post['email']
    if u_pwd1 == '' and u_pwd == '' and u_name == '' and u_email == '':
        # 未输入信息则重定向到注册页面
        return redirect('/user/register/')
    # 判断两次密码是否一致
    if u_pwd != u_pwd1:
        # 密码不一致则重定向到注册页面
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(u_pwd.encode('utf-8'))
    u_pwd_sha = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.u_name = u_name
    user.u_pwd = u_pwd_sha
    user.u_email = u_email
    user.save()
    # 重定向到登陆页面
    return redirect('/user/login/')


# 登陆请求处理
def login_handle(request):
    """
    登陆请求处理
    """
    # 接收用户输入
    post = request.POST
    u_name = post.get('name')
    u_pwd = post.get('pwd')
    # 判断用户是否选择记住用户名，默认值为0不选择
    check = post.get('check', 0)
    # 确认是否输入了信息
    if len(post) == 0:
        return redirect('/user/login/')
    # 密码加密
    s1 = sha1()
    s1.update(u_pwd.encode('utf-8'))
    u_pwd1 = s1.hexdigest()
    # 根据用户名来查询当前用户，使用filter的化假如对象不存在不会报异常返回空列表，而find会报异常
    user = UserInfo.objects.filter(u_name=u_name)
    if len(user) > 0:
        if user[0].u_pwd == u_pwd1:
            # 登陆成功，转到登陆之前的页面
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            # 记住用户名则设置用户名到cookie
            if check != 0:
                red.set_cookie('u_name', u_name)
            else:
                # 不保存用户名，max age用户信息立马过期
                red.set_cookie('u_name', '', max_age=-1)
            # 将用户登陆信息保存到session中
            request.session['user_id'] = user[0].id
            request.session['user_name'] = u_name
            return red
        else:
            # 用户密码错误
            context = {'tittle': '用户登陆', 'error_name': 0, 'error_pwd': 1, 'uname': u_name, 'upwd': u_pwd}
            return render(request, 'hh_user/login.html', context)
    else:
        # 用户账号错误
        context = {'tittle': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'uname': u_name, 'upwd': u_pwd}
        return render(request, 'hh_user/login.html', context)


# 判断传入的用户名是否存在
def register_exits(request):
    """
    判断传入的用户名是否存在
    返回为以该用户名进行查找的返回结果数量
    """
    u_name = request.GET['uname']
    count = UserInfo.objects.filter(u_name=u_name).count()
    return JsonResponse({'count': count})


# 保存用户信息
def save_user_info(request):
    """
    保存用户信息
    :param request:
    :return:
    """
    # 判断是否保存了用户的 session 信息
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    # 如果用户没有登陆则直接跳转到登陆界面
    if user_name == '':
        return redirect('/user/login/')
    # 获取用户信息
    user = UserInfo.objects.get(id=user_id)
    # 获取post请求过来的信息
    if request.POST:
        u_real_name = request.POST.get('u_name')
        u_addr = request.POST.get('u_addr')
        u_code = request.POST.get('u_code')
        u_phone = request.POST.get('u_phone')
        # 更新用户信息
        user.u_addr = u_addr
        user.u_real_name = u_real_name
        user.u_code = u_code
        user.u_phone = u_phone
        # 保存用户信息
        user.save()

    # 重定向到登陆页面
    return redirect('/user/site/')


# 用户退出
def exit(request):
    """
    用户退出登陆
    :param request:
    :return:
    """
    # 将用户信息从sessopn中删除
    request.session.flush()
    # 退出成功，转到主页
    return redirect('/')
