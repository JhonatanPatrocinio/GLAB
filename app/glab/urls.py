from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from base.viewsets import LaboratoryViewSet
from users.viewsets import UserViewSet
from users.views import LoginView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='UserApp')
router.register(r'laboratories', LaboratoryViewSet, basename='LaboratoryApp')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

