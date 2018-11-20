"""__author__=Zeng"""

from django.conf.urls import url

from order import views

urlpatterns = [
    # 添加到购物车
    url(r'^order/', views.order, name='order'),
]