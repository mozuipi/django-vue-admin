from django.shortcuts import render
from rest_framework import viewsets
from oAuth.models import NewUser
from rest_framework.response import Response

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