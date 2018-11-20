"""__author__=Zeng"""

from django.conf.urls import url

from goods import views

urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),
    # 详情页面
    url(r'^detail/(\d+)/', views.detail, name='detail'),
]