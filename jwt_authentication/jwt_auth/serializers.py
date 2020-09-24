from rest_framework import serializers
from . import models as auth


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = auth.Role
        fields = "__all__"


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = auth.UserInfo
        fields = "__all__"


