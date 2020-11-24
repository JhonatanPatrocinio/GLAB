from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from base.viewsets import LaboratoryViewSet
from reserve.viewsets import ReserveViewSet
from users.viewsets import UserViewSet

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='UserApp')
router.register(r'reservations', ReserveViewSet, basename='ReverseApp')
router.register(r'laboratories', LaboratoryViewSet, basename='LaboratoryApp')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

