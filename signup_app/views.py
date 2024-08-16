from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from .signup_serializer import signup_serializer
# Create your views here.


class SignupView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=signup_serializer

                


    