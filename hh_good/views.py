from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page


# 网站首页
def index(request):
    """
    项目首页
    :param request:
    :return:
    """
    # 查询首页所需的数据
    # 查询所有的列表信息
    type_list = TypeInfo.objects.all()
    # 查询各个分类下的商品信息的最新四条、最热四条
    type0 = type_list[0].goodinfo_set.order_by('-id')[0:4]
    type01 = type_list[0].goodinfo_set.order_by('-g_click')[0:4]
    type1 = type_list[1].goodinfo_set.order_by('-id')[0:4]
    type11 = type_list[1].goodinfo_set.order_by('-g_click')[0:4]
    type2 = type_list[2].goodinfo_set.order_by('-id')[0:4]
    type21 = type_list[2].goodinfo_set.order_by('-g_click')[0:4]
    type3 = type_list[3].goodinfo_set.order_by('-id')[0:4]
    type31 = type_list[3].goodinfo_set.order_by('-g_click')[0:4]
    type4 = type_list[4].goodinfo_set.order_by('-id')[0:4]
    type41 = type_list[4].goodinfo_set.order_by('-g_click')[0:4]
    type5 = type_list[5].goodinfo_set.order_by('-id')[0:4]
    type51 = type_list[5].goodinfo_set.order_by('-g_click')[0:4]
    # 构建首页信息内容
    context = {
        'title': '首页 禾禾生鲜',
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'hh_good/index.html', context)


# 商品列表页
def list(request, tid, pindex, sort):
    """
    列表页显示
    :param request:
    :param tid: 商品类型
    :param pindex: 第几页
    :param sort: 排序依据
    :return:
    """
    # 查询分类信息
    type_info = TypeInfo.objects.get(pk=int(tid))
    # 查询新品推荐
    news = type_info.goodinfo_set.order_by('-id')[0:2]
    if sort == '1':
        # 默认最新
        goods_list = GoodInfo.objects.filter(g_type_id=int(tid)).order_by('-id')
    elif sort == '2':
        # 价格
        goods_list = GoodInfo.objects.filter(g_type_id=int(tid)).order_by('-g_price')
    elif sort == '3':
        goods_list = GoodInfo.objects.filter(g_type_id=int(tid)).order_by('-g_click')
    # 构建分页器
    paginator = Paginator(goods_list, 10)
    # 获取当前分页页面对象
    page = paginator.page(int(pindex))
    # 构建返回数据
    content = {
        'title': type_info.t_title,
        'page': page,
        'paginator': paginator,
        'type_info': type_info,
        'sort': sort,
        'news': news,
        # 是否是详情页面
        'detail': False
    }
    return render(request, 'hh_good/list.html', content)


# 商品详情页
def detail(request, id):
    """
    商品详情页面所需数据
    :param request:
    :param id: 商品id
    :return:
    """
    # 查询当前商品对象
    good = GoodInfo.objects.get(pk=int(id))
    # 更新商品的点击量
    good.g_click = good.g_click+1
    good.save()
    # 查询当前商品对应的类别中最新的数据
    news = good.g_type.goodinfo_set.order_by('-id')[0:2]
    # 构造返回数据
    context = {
        'title': good.g_type.t_title,
        'good': good,
        'news': news,
        'id': id,
        # 是否是详情页面
        'detail': True
    }
    # 返回对象
    response = render(request, 'hh_good/detail.html', context)

    # 将当前商品记录到 cookie 中，首先读取 cookies 记录，默认为空字符串
    good_id_list = request.COOKIES.get('good_id_list', '')
    # 当前用户查看的商品id
    good_id = '%d'%good.id
    # 判断 cookies 中是否有数据
    if good_id_list != '':
        # 将已经访问的商品id切分为列表
        good_id_list_copy = good_id_list.split(',')
        # 假如该商品已经存在与cookies中则删除掉
        if good_id_list_copy.count(good_id) >= 1:
            good_id_list_copy.remove(good_id)
        # 将该商品插入到列表的第一个位置上
        good_id_list_copy.insert(0, good_id)
        # 如果商品超过6个则删除一个
        if len(good_id_list_copy) >= 6:
            del good_id_list_copy[5]
        # 将列表拼接为字符串
        good_id_list = ','.join(good_id_list_copy)
    else:
        good_id_list = good_id
    # 将 cookies 设置到response中
    response.set_cookie('good_id_list', good_id_list)

    return response
