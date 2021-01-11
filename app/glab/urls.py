from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

