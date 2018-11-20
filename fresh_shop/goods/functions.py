"""__author__=Zeng"""
from django.http import HttpResponseRedirect
from django.urls import reverse


def new_login_required(func):
    def check_login(request):
        try:
            # 验证cookie中的session值是否存在
            # 验证服务器端django_session表中是否存在对应的记录信息
            # 如果存在则获取是否设置的user_id值
            request.session['user_id']
            # request.session.get('user_id')
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)

    return check_login