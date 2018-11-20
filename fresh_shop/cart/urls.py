"""__author__=Zeng"""

from django.conf.urls import url

from cart import views

urlpatterns = [
    # 添加到购物车
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    # 购物车
    url(r'^carts/', views.carts, name='carts'),
    # 结算
    url(r'^place_order/', views.place_order, name='place_order'),
    # 刷新价格
    url(r'^f_price/', views.f_price, name='f_price'),
    # 购物车数据
    url(r'^cart_count/', views.cart_count, name='cart_count'),
    # 修改购物车中商品的个数
    url(r'^change_goods_num/', views.change_goods_num, name='change_goods_num'),
    # 删除购物车商品
    url(r'^cart_goods_del/(\d+)/', views.cart_goods_del, name='cart_goods_del'),
]