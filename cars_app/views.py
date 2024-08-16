from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import cars_table
from .car_serializer import car_serializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
class CarView(ModelViewSet):
    queryset=cars_table.objects.all()
    serializer_class=car_serializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]