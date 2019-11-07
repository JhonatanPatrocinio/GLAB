"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.base.views import home
from apps.users.api.viewsets import UserViewSet
from apps.base.api.viewsets import LaboratoryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='UserApp')
router.register(r'reservations', UserViewSet, base_name='ReverseApp')
router.register(r'laboratories', LaboratoryViewSet, base_name='LaboratoryApp')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

