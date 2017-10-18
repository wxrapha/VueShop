# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/17 下午11:28'


def get_auth_url():
    weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
    redirect_url = 'https://www.xiehaoo.com'
    auth_url = weibo_auth_url + '?client_id={client_id}&redirect_uri={re_url}'.format(client_id=3201777751, re_url=redirect_url)

    print(auth_url)


def get_access_token(code='8d9c27d2a8d84abe8fb8d208abff0903'):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    re_dict = requests.post(access_token_url, data={
        'client_id':3201777751,
        'client_secret': 'd6fcf58bd3335a003ab19fcbf392ec04',
        'grant_type':'authorization_code',
        'code': code,
        'redirect_uri':'https://www.xiehaoo.com'
    })

    #'{"access_token":"2.001eg1tCde1gUD21928a976aN4sTdC","remind_in":"157679999","expires_in":157679999,"uid":"2649894652","isRealName":"true"}'
    pass
def get_user_info(access_token='', uid=''):
    user_url = 'https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}'.format(token=access_token, uid=uid)
    print(user_url)

if __name__ == '__main__':
   # get_auth_url()
    #get_access_token(code='8d9c27d2a8d84abe8fb8d208abff0903')

    get_user_info(access_token="2.001eg1tCde1gUD21928a976aN4sTdC", uid="2649894652")