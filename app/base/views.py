from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from base.models import Reservation
from base.forms import ReservationForm


class DashboardStudentView(LoginRequiredMixin, ListView):
    template_name = 'perfil_discente.html'
    queryset = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)
    model = Reservation
    ordering = 'date'
    login_url = 'login'


class DashboardTeacherView(LoginRequiredMixin, ListView):
    template_name = 'perfil_docente.html'
    queryset = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)
    model = Reservation
    ordering = 'date'
    login_url = 'login'


class ReservationCreateView(CreateView):
    template_name = 'realizar_reserva.html'
    form_class = ReservationForm
    model = Reservation
    success_url = reverse_lazy('')

