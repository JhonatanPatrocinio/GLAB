from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import UploadToFactory
from .choices import TYPE_USERS


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=1, choices=TYPE_USERS)
    email_confirm = models.BooleanField(default=False)
    share_email = models.BooleanField(default=False)
    share_phone = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to=UploadToFactory('users/user/profile-picture'),
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('userApp')
        verbose_name_plural = _('usersApp')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
