# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/17 下午5:09'


from rest_framework import serializers
from goods.models import Goods
from .models import ShoppingCart
from goods.serializers import GoodsSerializer


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, min_value=1,label='数量',
                                    error_messages={
                                        'min_value':'商品数量不能小于1',
                                        'required':'请选择购买商品数量'
                                    })

    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all(), required=True, label='商品', help_text='商品')

    def create(self, validated_data):
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed =existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        #修改商品数量
        instance.nums = validated_data['nums']
        instance.save()
        return instance