from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from user.form import UserLoginForm


def login(request):
    if request.method == 'GET':
        # 返回登录页面
        return render(request, 'login.html')

    if request.method == 'POST':
        # 将请求参数丢给form表单做检验
        form = UserLoginForm(request.POST)
        # 校验结果，返回true表示检验成功
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if not user:
                # 没有user对象，表示验证密码不通过
                return render(request, 'login.html')
            # 实现登录，request.user等于登录用户对象
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:index'))
        else:
            errors = form.errors
            return render(request, 'login.html', {'errors': errors})


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')