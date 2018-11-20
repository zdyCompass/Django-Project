"""__author__=Zeng"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from goods import views

urlpatterns = [
    # 商品分类编辑
    url(r'^goods_category_detail/(\d+)/', views.goods_category_detail, name='goods_category_detail'),
    # 商品分类
    url(r'^goods_category_list/', views.goods_category_list, name='goods_category_list'),
    # 商品列表
    url(r'^goods_list/', views.goods_list, name='goods_list'),
    # 商品添加
    url(r'^goods_detail/', views.goods_detail, name='goods_detail'),
    # 删除商品
    url(r'^goods_del/(\d+)/', views.goods_del, name='goods_del'),
    # 编辑商品
    url(r'^goods_edit/(\d+)/', views.goods_edit, name='goods_edit'),
    # 商品描述
    url(r'^goods_desc/(\d+)/', views.goods_desc, name='goods_desc'),
]

