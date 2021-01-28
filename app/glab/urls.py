from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    LoginView, LogoutView, SignUpView, EditProfileView, DetailProfileView, ChangePasswordView
)
from base.views import (
    DashboardView, ReservationCreateView, ReservationListView, ReservationDetailView, ChoicePlaceView,
    LeaveReservationView, IndexView, ReservationView
)



reservation_patterns = ([
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('create/<int:place_id>', ReservationCreateView.as_view(), name='reservation_create'),
    path('detail/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('choice_place/', ChoicePlaceView.as_view(), name='reservation_choice_place'),
    path('delete/<int:pk>', LeaveReservationView.as_view(), name='reservation_leave'),

], 'reservation')

profile_patterns = ([
    path('', DetailProfileView.as_view(), name='detail_profile'),
    path('update/', EditProfileView.as_view(), name='update_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')

], 'profile')


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name='index'),
    path('view/<int:pk>', ReservationView.as_view(), name='view_reservation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('reservation/', include(reservation_patterns)),
    path('profile/', include(profile_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
