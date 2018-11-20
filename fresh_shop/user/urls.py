"""__author__=Zeng"""

from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),
    # 登录验证，获取登录系统的用户
    url('is_login/', views.is_login, name='is_login'),
    # 个人信息中心
    url('user_center_info/', views.user_center_info, name='user_center_info'),
    # 全部订单
    url('user_center_order/', views.user_center_order, name='user_center_order'),
    # 收获地址
    url('user_center_site/', views.user_center_site, name='user_center_site'),
]