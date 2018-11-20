"""__author__=Zeng"""

from django import forms
from django.contrib.auth.hashers import check_password

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True,
                               error_messages={'required': '用户名必填',
                                               'max_length': '用户名不能超过20个字符'})
    password = forms.CharField(max_length=255, required=True,
                               error_messages={'required': '注册密码必填',
                                               'max_length': '用户密码不能超过255个字符'})
    cpassword = forms.CharField(max_length=255, required=True,
                                error_messages={'required': '注册确认密码必填',
                                                'max_length': '用户密码不能超过255个字符'})
    email = forms.EmailField(max_length=100,
                             error_messages={'max_length': '邮箱名不能超过100个字符'})
    allow = forms.BooleanField()

    def clean(self):
        # 获取用户名，用户校验该用户是否已经注册
        name = self.cleaned_data.get('username')
        # 校验用户是否注册
        user = User.objects.filter(username=name).first()
        if user:
            raise forms.ValidationError({'username': '该账号已经注册'})
        # 验证密码是否一致
        if self.cleaned_data.get('password') != self.cleaned_data.get('cpassword'):
            raise forms.ValidationError({'password': '密码不一致'})
        if not self.cleaned_data.get('allow'):
            raise forms.ValidationError({'allow': '同意“天天生鲜用户使用协议”才能注册'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True,
                               error_messages={'required': '用户名必填',
                                               'max_length': '用户名不能超过20个字符'})
    password = forms.CharField(max_length=255, required=True,
                               error_messages={'required': '注册密码必填',
                                               'max_length': '用户密码不能超过255个字符'})

    def clean(self):
        # 获取用户名，用户校验该用户是否已经注册
        name = self.cleaned_data.get('username')
        # 校验用户是否注册
        user = User.objects.filter(username=name).first()
        if not user:
            raise forms.ValidationError({'username': '该账号未注册，请先注册'})
        # 验证密码是否一致
        if not check_password(self.cleaned_data.get('password'), user.password):
            raise forms.ValidationError({'password': '密码不一致'})
        return self.cleaned_data
