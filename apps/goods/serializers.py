# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/9 下午1:59'


from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
        sub_cat = CategorySerializer2(many=True)

        class Meta:
                model = GoodsCategory
                fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
        category = CategorySerializer()

        class Meta:
                model = Goods
                fields = "__all__"

