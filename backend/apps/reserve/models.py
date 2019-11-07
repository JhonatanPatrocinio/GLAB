from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import User
from apps.base.models import Laboratory


class Reserve(models.Model):
    user = models.ForeignKey(User, related_name='reserve_set', on_delete=models.PROTECT)
    laboratory = models.ForeignKey(Laboratory, related_name='reserve_set', on_delete=models.PROTECT)
    date = models.DateField(_('Start Date'))
    initial_time = models.DateTimeField(_('Initial Time'))
    end_time = models.DateTimeField(_('End Time'))
    status = models.CharField(_('Status'), max_length=1)
    obs = models.TextField(_('Obs'), max_length=255)

    # About OBJ
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _('Reserve')
        verbose_name_plural = _('Reservations')
