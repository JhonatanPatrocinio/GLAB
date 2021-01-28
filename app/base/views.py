from django.views.generic import ListView, CreateView, DetailView, FormView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
import calendar
from django_filters.views import FilterView

from base.models import Reservation, Place, TypePlace
from base.forms import ReservationForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        today = timezone.now()
        reservations = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)
        context['this_month'] = reservations.filter(date__month=today.month)
        context['this_week'] = reservations.filter(
            date__gte=today.date(), date__lte=(today.date() + timezone.timedelta(days=7))
        )
        return context


class ReservationView(DetailView):
    template_name = 'view_reservation.html'
    model = Reservation
    queryset = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)



class DashboardView(LoginRequiredMixin, ListView):
    queryset = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)
    model = Reservation
    template_name = 'index_dashboard.html'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context['last_solicitation'] = Reservation.objects.filter(user=self.request.user).last()
        today = timezone.now()
        reservations = Reservation.objects.filter(status=Reservation.RESPONSE_ACCEPTED)
        context['this_month'] = reservations.filter(date__month=today.month)
        context['this_week'] = reservations.filter(
            date__gte=today.date(), date__lte=(today.date() + timezone.timedelta(days=7))
        )
        return context


class ReservationListView(LoginRequiredMixin, ListView):
    template_name = 'reservation/reservation_list.html'
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reservation/create_reservation.html'
    form_class = ReservationForm
    model = Reservation
    success_url = reverse_lazy('reservation:reservation_list')

    def get_context_data(self, **kwargs):
        context = super(ReservationCreateView, self).get_context_data(**kwargs)
        context['object_place'] = get_object_or_404(Place, id=self.kwargs.get('place_id', None))
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        self.object = form.save(user=self.request.user, place=context['object_place'])
        messages.success(self.request, 'Reserva solicitada com sucesso')
        return HttpResponseRedirect(self.get_success_url())


class ReservationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'reservation/reservation_detail.html'
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ChoicePlaceView(LoginRequiredMixin, FilterView):
    template_name = 'reservation/choice_place.html'
    filterset_fields = ('type', )
    model = Place

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ChoicePlaceView, self).get_context_data(**kwargs)
        context['type_places'] = TypePlace.objects.all()
        return context


class LeaveReservationView(LoginRequiredMixin, DeleteView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = Reservation.RESPONSE_CANCELED
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('reservation:reservation_detail', kwargs={"pk": self.object.id})