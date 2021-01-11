import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .utils import UploadToFactory


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name,  password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, first_name=None, last_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField('ID', default=uuid.uuid4, primary_key=True)
    email = models.EmailField(
        _('Email'), unique=True, error_messages={
            'unique': _("A user with that email already exists.")
        }
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    is_staff = models.BooleanField(
        _('Status Equipe'), default=False, help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('Ativo'), default=True, help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        )
    )
    date_joined = models.DateTimeField(_('Criação da Conta'), default=timezone.now)
    email_confirm = models.BooleanField(_('Flag Email Confirmado'), default=False)
    share_email = models.BooleanField(_('Flag Compartilhar Email'), default=False)
    share_phone = models.BooleanField(_('Flag Compartilhar Telefone'), default=False)
    phone_number = models.CharField(_('Número de Telefone'), max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(
        _('Foto de Perfil'), upload_to=UploadToFactory('users/user/profile-picture'), null=True
    )
    description = models.CharField(_('Descrição'), max_length=255, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ordering = ['first_name']
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def get_type(self):
        if hasattr(self, 'teacher_set'):
            return 'T'
        elif hasattr(self, 'student_set'):
            return 'S'
        elif self.is_staff:
            return 'A'


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Username'), related_name='teacher_set')
    registry_id = models.CharField(_('Matricula'), max_length=11, validators=[RegexValidator(r'\D')])

    class Meta:
        ordering = ['user']
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teacher\'s')

    def __str__(self):
        return f'{self.user.first_name}'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Username'), related_name='student_set')
    registry_id = models.CharField(_('Matricula'), max_length=11, validators=[RegexValidator(r'\D')])

    class Meta:
        ordering = ['user']
        verbose_name = _('Student')
        verbose_name_plural = _('Student\'s')

    def __str__(self):
        return f'{self.user.first_name}'


