from django.shortcuts import render
from rest_framework import viewsets
from oAuth.models import (
    NewUser,
    WechatManager,
    DingTalkManager
)
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from oAuth.serializers import WechatTokenObtainSerializer
from urllib.parse import quote
import base64
from Crypto.Cipher import AES

# Create your views here.


class UserInfoViewSet(viewsets.ViewSet):
    queryset = NewUser.objects.all().order_by('-date_joined')
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        print('ok')
        user_info = NewUser.objects.filter(id=request.user.id).values()[0]
        role = request.user.roles
        if role == 0:
            user_info['roles'] = ['admin']
        else:
            user_info['roles'] = ['user']
        user_info['name'] = user_info['first_name'] + user_info['last_name']

        return Response(user_info)


class WechatTokenObtainPairView(TokenObtainPairView):

    serializer_class = WechatTokenObtainSerializer

class QRcodeViewSet(viewsets.ViewSet):
    queryset = WechatManager.objects.all()
    http_method_names = ['get']
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        dingtalk_manager_info = DingTalkManager.objects.all()
        data = {
            'wechat_qr_code_url': '',
            'dingtalk_qr_code_url': ''
        }
        try:
            wechat_redirect_uri = quote(request.META['HTTP_DOMAIN'] + '/wechat/login', safe='')
            dingtalk_redirect_uri = quote(request.META['HTTP_DOMAIN'] + '/dingtalk/login', safe='')
            # dingtalk_qr_code_url: 'https://login.dingtalk.com/oauth2/challenge.htm?redirect_uri=https%3A%2F%2Fwechat.huoxingxiaoliu.com%2Fdingtalk%2Flogin&response_type=code&client_id=dingp26p2zhj5cyh2odk&scope=openid&state=DingTalk&prompt=consent'
            if self.queryset.exists():
                wechat_manager_info = self.queryset.values()[0]
                wechat_qr_code_url = 'https://open.work.weixin.qq.com/wwopen/sso/qrConnect?appid=%s&agentid=%s&redirect_uri=%s&state=Wechat#wechat_redirect' %(wechat_manager_info['appid'], wechat_manager_info['agentid'], wechat_redirect_uri)
                # dingtalk_qr_code_url = 'https://login.dingtalk.com/oauth2/challenge.htm?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=DingTalk&prompt=consent' % (wechat_manager_info['appid'], wechat_)
                # return Response({'wechat_qr_code_url': wechat_qr_code_url}, status=200)
                data['wechat_qr_code_url'] = wechat_qr_code_url

            if dingtalk_manager_info.exists():
                dingtalk_manager_info = dingtalk_manager_info[0]
                dingtalk_qr_code_url = 'https://login.dingtalk.com/oauth2/challenge.htm?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=DingTalk&prompt=consent' % (dingtalk_redirect_uri, dingtalk_manager_info.client_id)
                data['dingtalk_qr_code_url'] = dingtalk_qr_code_url

            return Response(data, status=200)
        except Exception as e:
            return Response(data, status=200)

class CheckViewSet(viewsets.ViewSet):
    queryset = WechatManager.objects.all()
    http_method_names = ['post']
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        signature = request.query_params.get('signature')
        msg_signature = request.query_params.get('msg_signature')
        timestamp = request.query_params.get('timestamp')
        nonce = request.query_params.get('nonce')
        request_data = dict(request.data, **request.query_params)
        encrypt = request.data.get('encrypt')
        encrypt_decode = base64.b64decode(encrypt)
        return Response(request.query_params)
