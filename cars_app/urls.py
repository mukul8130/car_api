from rest_framework.routers import DefaultRouter
from .views import CarView

router= DefaultRouter()

router.register("car_view",CarView,basename= "car")