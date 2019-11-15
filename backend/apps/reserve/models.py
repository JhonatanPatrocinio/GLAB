from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from apps.users.models import User
from apps.base.models import Laboratory
from .choices import STATUS_RESERVE_CHOICES


class Reserve(models.Model):
    user = models.ForeignKey(User, related_name='reserve_set', on_delete=models.PROTECT, verbose_name=_('Utilizador'))
    laboratory = models.ForeignKey(Laboratory, related_name='reserve_set', on_delete=models.PROTECT, verbose_name=_('Laboratório'))
    date = models.DateField(_('Data'))
    initial_time = models.TimeField(_('Hora Inicio'))
    end_time = models.TimeField(_('Hora Termino'))
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_RESERVE_CHOICES, default=1)
    obs = models.TextField(_('Observações'), max_length=255)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Reserva')
        verbose_name_plural = _('Reservas')

    def __str__(self):
        return f'{self.user.first_name} - {self.laboratory.name}'

    def save(self, *args, **kwargs):
        if self.created_at:
            self.update_at = datetime.now()
        return super(Reserve, self).save(*args, **kwargs)
