from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.base.views import home
from apps.users.api.viewsets import UserViewSet
from apps.base.api.viewsets import LaboratoryViewSet
from apps.reserve.api.viewsets import ReserveViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='UserApp')
router.register(r'reservations', ReserveViewSet, base_name='ReverseApp')
router.register(r'laboratories', LaboratoryViewSet, base_name='LaboratoryApp')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

