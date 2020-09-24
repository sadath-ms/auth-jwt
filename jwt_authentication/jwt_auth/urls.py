from django.urls import path
from . import (
    views,
    auth
)

urlpatterns = [
    path("add-roles/", views.CreateRoleApi.as_view()),
    path("user-signup/", views.UserSignUp.as_view()),
    path("user-sign-in/", auth.UserSignIn.as_view()),
]

