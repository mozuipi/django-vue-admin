from oAuth.models import NewUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    class Meta:
        model = NewUser
        fields = ['url', 'username', 'email', 'is_staff', 'name']
