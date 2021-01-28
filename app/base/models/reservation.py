from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Reservation(models.Model):
    RESPONSE_WAITING = 1
    RESPONSE_DENIED = 2
    RESPONSE_ACCEPTED = 3
    RESPONSE_CANCELED = 4

    STATUS_RESERVE_CHOICES = [
        (RESPONSE_WAITING, _('Aguardando Resposta')),
        (RESPONSE_DENIED, _('Utilização Negada')),
        (RESPONSE_ACCEPTED, _('Utilização Aceita')),
        (RESPONSE_CANCELED, _('Cancelado pelo usuário'))
    ]
    place = models.ForeignKey('base.Place', on_delete=models.PROTECT, verbose_name=_('Nome do Espaço'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('Solicitante'))
    phone = models.CharField(_('Telefone'), max_length=16, help_text=_('Informe um telefone para contato'))
    date = models.DateField(_('Data'))
    initial_time = models.TimeField(_('Hora Inicio'))
    end_time = models.TimeField(_('Hora Término'))
    status = models.IntegerField(_('Status'), choices=STATUS_RESERVE_CHOICES, default=1)
    reason = models.TextField(_('Motivo'), max_length=400)
    obs = models.TextField(_('Observações'), max_length=355, blank=True)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['date']
        verbose_name = _('Reserva')
        verbose_name_plural = _('Reservas')

    def __str__(self):
        return f'{self.user} - {self.place.name}'

    def save(self, *args, **kwargs):
        if self.created_at:
            self.update_at = timezone.now()
        return super().save(*args, **kwargs)

    def clean(self):
        if self.id and Reservation.objects.filter(
                date=self.date, initial_time__range=([self.initial_time, self.end_time]),
                status=self.RESPONSE_ACCEPTED).exclude(id=self.id).exists():
            raise ValidationError(_('Já existe uma reserva confirmada neste horário'))

        return super().clean()

    @property
    def get_start_date(self):
        return timezone.datetime(
            self.date.year, self.date.month, self.date.day, self.initial_time.hour, self.initial_time.minute
        )

    @property
    def get_end_date(self):
        return timezone.datetime(
            self.date.year, self.date.month, self.date.day, self.end_time.hour, self.end_time.minute
        )

    @property
    def get_date_display(self):
        return f'{self.date.strftime("%d/%m/%Y")} ' \
               f'{self.initial_time.strftime("%H:%M")} - {self.end_time.strftime("%H:%M")}'

    @property
    def get_text_status_color(self):
        if self.status == Reservation.RESPONSE_WAITING:
            return 'text-warning'
        elif self.status == Reservation.RESPONSE_ACCEPTED:
            return 'text-success'
        elif self.status == Reservation.RESPONSE_DENIED:
            return 'text-danger'
        elif self.status == Reservation.RESPONSE_CANCELED:
            return 'text-danger'
        else:
            return ''

    @property
    def get_absolute_url(self):
        return reverse("view_reservation", kwargs={"pk": self.pk})
