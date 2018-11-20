
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from user.forms import UserRegisterForm, UserLoginForm
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 将页面中提交的参数交给form表单做验证
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # 检验通过，对密码进行加密
            password = make_password(form.cleaned_data.get('password'))
            User.objects.create(username=form.cleaned_data.get('username'),
                                password=password,
                                email=form.cleaned_data.get('email'))
            return HttpResponseRedirect(reverse('user:login'))
        else:
            # 验证不通过
            return render(request, 'register.html', {'errors': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # 验证通过，进行会话
            request.session['user_id'] = User.objects.filter(username=form.cleaned_data.get('username')).first().id
            return HttpResponseRedirect(reverse('goods:index'))
        return render(request, 'login.html', {'errors': form.errors})


def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('goods:index'))


def is_login(request):
    if request.method == 'GET':
        # 清空session
        user = request.user
        return JsonResponse({'code': 200, 'msg': '请求成功', 'username': user.username})


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')


def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'user_center_site.html')