"""car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from cars_app.urls import router
from signup_app.urls import router1
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api1/',include(router1.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view())
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
