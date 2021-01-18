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
        _('Email Institucional'), unique=True, error_messages={
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
    def get_type(self):
        if self.teacher_set.exists():
            return 'T'
        elif self.student_set.exists():
            return 'S'
        elif self.is_staff:
            return 'A'
        else:
            return None

    def get_user_url(self):
        type_user = self.get_type
        if type_user == 'T':
            return reverse_lazy('teacher:dashboard_teacher')
        elif type_user == 'S':
            return reverse_lazy('students:dashboard_student')
        else:
            return reverse_lazy('admin:index')


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Username'), related_name='teacher_set')
    registry = models.CharField(_('Matricula'), max_length=11, validators=[RegexValidator(r'\D', inverse_match=True)])
    academic_center = models.ForeignKey(
        'base.AcademicCenter', related_name='teacher_set', verbose_name=_('Centro Acadêmico'),
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['user']
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')

    def __str__(self):
        return f'{self.user.full_name}'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='student_set')
    registry = models.CharField(_('Matricula'), max_length=11, validators=[RegexValidator(r'\D', inverse_match=True)])
    course = models.ForeignKey(
        'base.Course', verbose_name=_('Curso'), on_delete=models.PROTECT, related_name='student_set'
    )

    class Meta:
        ordering = ['user']
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')

    def __str__(self):
        return f'{self.user.full_name}'


