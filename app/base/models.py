from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class AcademicCenter(models.Model):
    name = models.CharField(_('Nome'), max_length=200)
    shortening = models.CharField(_('Sigla'), max_length=10)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['shortening']
        verbose_name = 'Centro Acadêmico'
        verbose_name_plural = 'Centros Acadêmicos'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.created_at:
            self.updated_at = timezone.now()
        return super(AcademicCenter, self).save(*args, **kwargs)


class Course(models.Model):
    cod = models.CharField(_('Código'), max_length=10)
    name = models.CharField(_('Nome'), max_length=170)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f'{self.cod} - {self.name}'

    def save(self, *args, **kwargs):
        if self.created_at:
            self.update_at = timezone.now()
        return super(Course, self).save(*args, **kwargs)


class Laboratory(models.Model):
    name = models.CharField(_('Nome'), max_length=120)
    n_computers = models.IntegerField(_('Número de Computadores'), validators=[MinValueValidator(0)], default=0)
    capacity = models.IntegerField(_('Capacidade de pessoas'), validators=[MinValueValidator(0)], default=0)

    class Meta:
        ordering = ['name']
        verbose_name = _('Laboratório')
        verbose_name_plural = _('Laboratórios')

    def __str__(self):
        return f'{self.name}'


class Reservation(models.Model):
    RESPONSE_WAITING = 1
    RESPONSE_DENIED = 2
    RESPONSE_ACCEPTED = 3
    UTILIZED = 4
    STATUS_RESERVE_CHOICES = [
        (RESPONSE_WAITING, _('Aguardando Resposta')),
        (RESPONSE_DENIED, _('Utilização Negada')),
        (RESPONSE_ACCEPTED, _('Utilização Aceita')),
        (UTILIZED, _('Utilizado'))
    ]
    user = models.ForeignKey(
        User, related_name='reservation_set', on_delete=models.PROTECT, verbose_name=_('Utilizador')
    )
    laboratory = models.ForeignKey(
        Laboratory, related_name='reservation_set', on_delete=models.PROTECT, verbose_name=_('Laboratório')
    )
    date = models.DateField(_('Data'))
    initial_time = models.TimeField(_('Hora Inicio'))
    end_time = models.TimeField(_('Hora Termino'))
    status = models.IntegerField(_('Status'), choices=STATUS_RESERVE_CHOICES, default=1)
    reason = models.TextField(_('Motivo'), max_length=400)
    obs = models.TextField(_('Observações'), max_length=355, blank=True)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['user', 'date']
        verbose_name = _('Reserva')
        verbose_name_plural = _('Reservas')

    def __str__(self):
        return f'{self.user.full_name} - {self.laboratory.name}'

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

    # @property
    # def get_absolute_url(self):
    #     return reverse("dashboard_student", kwargs={"pk": self.pk})
