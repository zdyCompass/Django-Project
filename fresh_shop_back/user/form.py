"""__author__=Zeng"""
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    # 定义一个name字段，设置name字段的最大值和最小值
    # required是否必填
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={'required': '账号必填',
                                               'min_length': '账号长度不能短与两个字符',
                                               'max_length': '账号长度不能长于十个字符'})

    password = forms.CharField(required=True,
                               error_messages={'required': '密码必填'})

    def clean(self):
        # 使用django自带的User模块进行验证
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username': '该账号没有注册，无法登录'})

        return self.cleaned_data
