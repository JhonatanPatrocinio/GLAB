"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from apps.users.api.viewsets import UserViewSet, UserAppViewSet


router = routers.DefaultRouter()
router.register(r'users', UserAppViewSet, base_name='UserApp')
router.register(r'user', UserViewSet, base_name='User')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

