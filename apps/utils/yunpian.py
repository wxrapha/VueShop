# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/15 下午6:12'

import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def sned_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【xiehao博客】您的验证码是#code#。如非本人操作，请忽略本短信'.format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian("2ee7b8ed7ca025642c2b53cc5c134010")
    yun_pian.sned_sms('2017', '15062255019')