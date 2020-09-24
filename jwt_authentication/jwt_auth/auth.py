import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.serializers import (
    jwt_payload_handler,
    VerifyJSONWebTokenSerializer,
)
from rest_framework import generics, status
from . import models as auth
from rest_framework.response import Response


class UserSignIn(generics.CreateAPIView):

    def __init__(self):
        self.user_id = self.username = self.password = None
        super(UserSignIn, self).__init__()

    def check_user_exists(self):
        """
        to check user is register or not
        """
        is_exists = False
        if auth.UserInfo.objects.filter(
            user_id__username=self.username,
            is_active=True).exists():
            is_exists = True
        return is_exists

    def get_user_details(self):
        payload = jwt_payload_handler(self.user_id)
        token = jwt.encode(payload, settings.SECRET_KEY)
        user_details = {
            "user_id": self.user_id.id,
            "first_name": self.user_id.first_name,
            "token": token,
            "role": self.user_id.userpermissions.role_id.role_name
        }
        return user_details

    def create(self, request, *args, **kwargs):
        request_data = self.request.data
        self.username = request_data.get("username")
        self.password = request_data.get("password")
        if self.check_user_exists():
            self.user_id = authenticate(
                request=request, username=self.username, password=self.password
            )
            if self.user_id:
                login(request, self.user_id)
                result = {
                    'user_details': self.get_jwt_token()
                }
                response = {
                    'status_code': status.HTTP_200_OK,
                    'message': "Successfully logged in",
                    'result': result
                }
            else:
                response = {
                    'status_code': status.HTTP_404_NOT_FOUND,
                    'message': "invalid username and password",
                    'result': {}
                }
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': "Please register",
                'result': {}
            }
        return Response(response, status=response.get('status_code'))






