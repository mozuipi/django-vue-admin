from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from oAuth.models import (
    NewUser,
    Wechat,
    WechatManager
)

# Register your models here.


class NewUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'wechat', 'first_name', 'last_name' )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'roles')}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )

    list_display = ('id', 'username', 'wechat', 'roles', 'email', 'is_active', 'last_login')
    list_display_links = ('id', 'username', 'wechat', 'roles', 'email', 'last_login')
    search_fields = ('username', 'email', 'wechat')


admin.site.register(NewUser, NewUserAdmin)

class WechatAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid')
    list_display_links = ('id', 'userid')

admin.site.register(Wechat, WechatAdmin)

class WechatManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'appid', 'agentid', 'corpsecret')
    list_display_links = ('id', 'appid', 'agentid', 'corpsecret')

admin.site.register(WechatManager, WechatManagerAdmin)