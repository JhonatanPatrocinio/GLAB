import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, full_name,  password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not full_name:
            raise ValueError('The given first name must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, full_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, full_name, password, **extra_fields)

    def create_superuser(self, email, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, full_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField('ID', default=uuid.uuid4, primary_key=True)
    email = models.EmailField(
        _('Email'), unique=True, error_messages={
            'unique': _("Já existe um usuário com este email.")
        }
    )
    full_name = models.CharField(_('Nome'), max_length=30)
    is_staff = models.BooleanField(
        _('Status Equipe'), default=False, help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('Ativo'), default=True, help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        )
    )
    date_joined = models.DateTimeField(_('Criação da Conta'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        ordering = ['full_name']
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return f'{self.full_name}'

    @property
    def get_short_name(self):
        return self.full_name.split()[0]

    @property
    def get_requester(self):
        return self.requester_set
