from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator


class Laboratory(models.Model):
    name = models.CharField(_('Nome'), max_length=120, unique=True)
    n_computers = models.IntegerField(_('Número de Computadores'), validators=[MinValueValidator(0), ])

    class Meta:
        verbose_name = _('Laboratório')
        verbose_name_plural = _('Laboratórios')

    def __str__(self):
        return f'{self.name}'


