from django.shortcuts import render

# Create your views here.

from rest_framework import (
    generics,
    status
)
from rest_framework.response import Response
from . import serializers
from . import models as auth
from django.db import models as db_models
from django.contrib.auth.models import User


class CreateRoleApi(generics.CreateAPIView):
    serializer_class = serializers.RoleSerializer
    queryset = auth.Role.objects.all()


class UserSignUp(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer

    def if_user_exists(self):
        try:
            auth.UserInfo.objects.get(
                db_models.Q(user__username=self.request.data.get('mobile'))
                | db_models.Q(user__email=self.request.data.get('email')))
            is_exists = True
        except auth.UserInfo.DoesNotExist:
            is_exists = False
        return is_exists

    def create(self, request, *args, **kwargs):
        request_data = self.request.data
        if not self.if_user_exists():
            get_or_create_auth_user = User(
                username=request_data.get('mobile'),
                email=request_data.get('email'),
                first_name=request_data.get('name')
            )
            get_or_create_auth_user.set_password(request_data.get('password'))
            get_or_create_auth_user.save()
            request_data['user'] = get_or_create_auth_user.id
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Signup successful",
                'result': serializer.data
            }
        else:
            response = {
                'status_code': status.HTTP_409_CONFLICT,
                'message': "This username is already registered",
                'result': {}
            }
        return Response(response)













