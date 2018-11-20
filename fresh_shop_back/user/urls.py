"""__author__=Zeng"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from user import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),
    # 首页，login_required进行登录验证
    url(r'^index/', login_required(views.index), name='index')
]