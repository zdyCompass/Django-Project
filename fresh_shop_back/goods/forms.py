"""__author__=Zeng"""
from django import forms

from goods.models import Goods, GoodsCategory


class GoodsForm(forms.Form):
    # 商品名称
    name = forms.CharField(max_length=100, required=True,
                           error_messages={'required': '商品名必须填写',
                                           'max_length': '商品名不能超过100个字符'})
    # 商品货号
    goods_sn = forms.CharField(max_length=50, required=True,
                               error_messages={'required': '商品货号必须填写',
                                               'max_length': '商品名不能超过50个字符'})
    # 商品分类
    category = forms.CharField(required=True,
                               error_messages={'required': '商品分类必须填写'})
    # 商品库存
    goods_nums = forms.CharField(required=True,
                                 error_messages={'required': '商品库存必须填写'})
    # 商品价格
    market_price = forms.FloatField(required=True,
                                    error_messages={'required': '商品价格必须填写'})
    # 本店价格
    shop_price = forms.FloatField(required=True,
                                  error_messages={'required': '本店价格必须填写'})
    # 商品描述
    goods_brief = forms.CharField(max_length=500, required=True,
                                  error_messages={'required': '商品描述必须填写',
                                                  'max_length': '商品描述不能超过500个字符'})
    # 商品图片
    goods_front_image = forms.ImageField(required=False)

    # 创建方法二的步骤
    def clean_category(self):
        id = self.cleaned_data.get('category')
        cayegory = GoodsCategory.objects.filter(pk=id).first()
        return cayegory

    # def clean(self):
    #     # 获取商品名称
    #     name = self.cleaned_data.get('name')
    #     # 检验该商品是否存在
    #     goods = Goods.objects.filter(name=name).first()
    #     if goods:
    #         raise forms.ValidationError({'name': '该商品名已经存在'})
    #     goods_sn = self.cleaned_data.get('goods_sn')
    #     goods = Goods.objects.filter(goods_sn=goods_sn).first()
    #     if goods:
    #         raise forms.ValidationError({'name': '该商品编号已存在'})
    #     return self.cleaned_data




