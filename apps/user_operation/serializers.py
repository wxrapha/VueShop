# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/16 下午5:43'

import re
from VueShop.settings import REGEX_MOBILE
from rest_framework import serializers
from .models import UserFav, UserLeavingMessage, UserAddress
from rest_framework.validators import UniqueTogetherValidator
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已收藏'
            )
        ]
        fields = ('user', 'goods', 'id')


class LeavingMseeageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage

        fields = ('user', 'message_type', 'subject', 'message', 'file', 'id', 'add_time')


class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    signer_mobile = serializers.CharField(max_length=11)


    class Meta:
        model = UserAddress

        fields = ('user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time', 'id')



