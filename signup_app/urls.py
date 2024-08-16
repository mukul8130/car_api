from rest_framework.routers import DefaultRouter
from .views import SignupView

router1= DefaultRouter()

router1.register("sv",SignupView,basename= "signup")