from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Requester(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='requester_set')
    department = models.ForeignKey('base.Department', on_delete=models.PROTECT, verbose_name=_('Setor'))
    registry = models.CharField(_('Matricula'), max_length=11, validators=[RegexValidator(r'\D', inverse_match=True)])

    class Meta:
        ordering = ['user']
        verbose_name = _('Solicitante')
        verbose_name_plural = _('Solicitantes')

    def __str__(self):
        return f'{self.user} - {self.department}'
