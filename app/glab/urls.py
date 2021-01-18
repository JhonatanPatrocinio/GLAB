from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    LoginView, LogoutView, ChoiceSignUpView, TeacherSignUpView, StudentSignUpView, StudentEditProfileView,
    TeacherEditProfileView
)
from base.views import DashboardStudentView, DashboardTeacherView, ReservationCreateView


signup_patterns = ([
    path('', ChoiceSignUpView.as_view(), name='choice_signup'),
    path('teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('student/', StudentSignUpView.as_view(), name='student_signup'),
], 'signup')

student_patterns = ([
    path('', DashboardStudentView.as_view(), name='dashboard_student'),
    path('profile/', StudentEditProfileView.as_view(), name='edit_profile_student')

], 'students')

teacher_patterns = ([
    path('', DashboardTeacherView.as_view(), name='dashboard_teacher'),
    path('profile/', TeacherEditProfileView.as_view(), name='edit_profile_teacher'),
    path('reservation/', ReservationCreateView.as_view(), name='reservation_create_teacher')

], 'teacher')

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', include(signup_patterns)),
    path('student/', include(student_patterns)),
    path('teacher/', include(teacher_patterns))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
