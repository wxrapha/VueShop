# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/15 下午7:29'
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from VueShop.settings import REGEX_MOBILE
from datetime import datetime, timedelta
from .models import VerifyCode
from rest_framework.validators import UniqueValidator

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobine(self, mobile):
        """
        验证手机号码
        :param data;
        :return
        """

        #手机是否注册
        if User.object.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已存在')
        #验证手机号码是否正确
        if re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')
        #验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError('距离上一次放松未超过60S')

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4, help_text='验证码')
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已经存在')])

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by("-add_time")

        if verify_records:
            last_record = verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago < last_record.add_time:
                raise serializers.ValidationError('验证码已过期')
            if last_record.code != code:
                raise serializers.ValidationError('验证码错误')

        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'code', 'mobile')