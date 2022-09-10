from django.shortcuts import render
from rest_framework import viewsets
from oAuth.models import (
    NewUser,
    WechatManager
)
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from oAuth.serializers import WechatTokenObtainSerializer
from urllib.parse import quote

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
        redirect_uri = quote(request.META['HTTP_REFERER'] + '#/wechat/login', safe='')
        if self.queryset.exists():
            wechat_manager_info = self.queryset.values()[0]
            wechat_qr_code_url = 'https://open.work.weixin.qq.com/wwopen/sso/qrConnect?appid=%s&agentid=%s&redirect_uri=%s&state=django-vue-admin#wechat_redirect' %(wechat_manager_info['appid'], wechat_manager_info['agentid'], redirect_uri)
            return Response({'wechat_qr_code_url': wechat_qr_code_url}, status=200)
        else:
            return Response(False, status=200)
