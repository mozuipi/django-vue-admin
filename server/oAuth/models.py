from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class NewUser(AbstractUser):

    role_type = [
        [0, 'admin'],
        [1, 'user'],
    ]

    roles = models.IntegerField(verbose_name='角色', choices=role_type, default=1)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True, auto_now=True)
    wechat = models.ForeignKey('WeChat', null=True, blank=True, on_delete=models.SET_NULL)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass

class Wechat(models.Model):
    userid = models.CharField(verbose_name='企业微信id', max_length=99, unique=True)

    def __str__(self):
        return str(self.id) + '---' + self.userid

    class Meta:
        verbose_name_plural = "用户的微信信息"


class WechatManager(models.Model):
    appid = models.CharField(verbose_name='企业微信id', max_length=99, unique=True)
    agentid = models.CharField(verbose_name='企业微信应用id', max_length=99, unique=True)
    corpsecret = models.CharField(verbose_name='企业微信应用secret', max_length=99, unique=True)

    class Meta:
        verbose_name_plural = "微信管理信息（企业微信登录必填）"