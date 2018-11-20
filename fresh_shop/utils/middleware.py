"""__author__=Zeng"""
import re

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import User
from cart.models import ShoppingCart


class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # TODO: 某些页面需要登录才能访问，某些页面不需要登录就可以访问
        # TODO: 需要登录的页面，当用户没有登录时，该如何处理？
        # 给request.user赋值，赋的值为当前登录系统的用户对象
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            # 将user变为一个全局变量，如在index页面中登录后有欢迎XXX
            request.user = user
            # 可以访问所有的页面
            return None

        # 没有登录，即没有user_id

        # 思路：首页，详情，登录，注册页面，访问media，访问static，不管登录与否都可以查看
        # 下单，结算，订单页面，个人中心页面只能登录才能查看，没有登录就跳转到登录页面
        not_need_path = ['/user/login/', '/user/register/',
                         '/goods/index/', '/goods/detail/(.*)/',
                         '/media/(.*)', '/static/(.*)',
                         '/cart/add_cart/', '/cart/carts/',
                         '/cart/cart_count/', '/cart/f_price/',
                         '/cart/change_goods_num/', '/cart/cart_goods_del/']
        path = request.path
        for not_path in not_need_path:
            # 匹配当前路径是否为不需要登录验证的路径
            if re.match(not_path, path):
                return None
            # 当前的请求url不在not_need_path中，则表示当前url需要登录才能访问
        return HttpResponseRedirect(reverse('user:login'))


class SessionUpdate(MiddlewareMixin):

    def process_request(self, request):
        # session中商品数据和购物车表中数据的同步操作
        # session中数据结构：[[id, num, is_select], [id, num, is_select]]
        session_goods = request.session.get('goods')
        user_id = request.session.get('user_id')
        if user_id:
            # 用户登录后，才做同步
            if session_goods:
                # 思路：时刻保持session中数据和数据库中数据同步
                # 如果session中商品已经存在于数据库表中，则更新
                # 如果session中商品不存在与数据库中，则添加
                # 如果session中商品少于数据库中的商品，则更新session

                # 将session中数据同步到数据库
                for goods in session_goods:
                    # goods的结构[id, num, is_select]
                    cart = ShoppingCart.objects.filter(user_id=user_id,
                                                       goods_id=goods[0]).first()
                    if cart:
                        # 数据库中能查询到该商品信息，则修改
                        cart.nums = goods[1]
                        cart.is_select = goods[2]
                        cart.save()
                    else:
                        # 数据库总查询不到该商品信息，则修改
                        ShoppingCart.objects.create(user_id=user_id,
                                                    goods_id=goods[0],
                                                    nums=goods[1],
                                                    is_select=goods[2])
            # 将数据库数据同步到session中
            carts = ShoppingCart.objects.filter(user_id=user_id).all()
            # session中数据结构：[[id, num, is_select], [id, num, is_select]]
            session_new_goods = [[cart.goods_id, cart.nums, cart.is_select] for cart in carts]
            request.session['goods'] = session_new_goods

        return None

