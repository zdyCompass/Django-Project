from django.shortcuts import render

from goods.functions import new_login_required
from goods.models import GoodsCategory, Goods


def index(request):
    if request.method == 'GET':
        # categorys = GoodsCategory.objects.all()
        # goods = Goods.objects.all()
        # category_goods = {}
        # for category in categorys:
        #     goods_list = []
        #     for good in goods:
        #         if category.category_type == good.category_id:
        #             goods_list.append(good)
        #         category_goods[category] = goods_list
        categorys = GoodsCategory.CATEGORY_TYPE
        goods = Goods.objects.all()
        goods_dict = {}
        for category in categorys:
            goods_list = []
            count = 0
            for good in goods:
                # 判断商品分类和商品对象
                if category[0] == good.category.id and count < 4:
                    goods_list.append(good)
                    count += 1
            goods_dict[category[1]] = goods_list
        return render(request, 'index.html', {'goods_dict': goods_dict})


def detail(request, id):
    if request.method == 'GET':
        # 产看商品详情，返回商品对象
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'detail.html', {'goods': goods})
