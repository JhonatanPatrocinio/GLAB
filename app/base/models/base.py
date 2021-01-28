from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hall(BaseModel):
    full_name = models.CharField(_('Nome Completo'), max_length=200)
    short_name = models.CharField(_('Nome Conhecido'), max_length=50, null=True, blank=True)
    map_link = models.URLField(_('Link do Mapa'))

    class Meta:
        ordering = ['short_name']
        verbose_name = _('Bloco')
        verbose_name_plural = _('Blocos')

    def __str__(self):
        return f'{self.full_name}'


class Department(BaseModel):
    name = models.CharField(_('Nome'), max_length=200)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='department_set', verbose_name=_('Hall'))
    maintainer = models.CharField(_('Responsável'), max_length=100)
    contact = models.CharField(_('Contato'), max_length=16)

    class Meta:
        ordering = ['name']
        verbose_name = _('Setor')
        verbose_name_plural = _('Setores')

    def __str__(self):
        return f'{self.name}'


class TypePlace(BaseModel):
    name = models.CharField(_('Nome'), max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Tipo de Espaço')
        verbose_name_plural = _('Tipos de Espaços')

    def __str__(self):
        return f'{self.name}'

    @property
    def get_type(self):
        if self.name.lower() == 'auditorio':
            return 'A'
        elif self.name.lower() == 'laboratório':
            return 'L'
        elif self.name.lower() == 'quadra':
            return 'Q'
        else:
            return ''


class Place(BaseModel):
    class TypeCourt(models.TextChoices):
        MULTISPORT = 'M', _('Quadra Poliesportiva')
        VOLLEY = 'V', _('Volei')
        FUTSAL = 'F', _('Futsal')
        BASKETBALL = 'B', _('Basquete')
        NO = 'N', _('Nenhuma')

    name = models.CharField(_('Nome do Espaço'), max_length=200)
    type = models.ForeignKey(
        TypePlace, on_delete=models.PROTECT, related_name='place_set', verbose_name=_('Tipo de Espaço')
    )
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name='place_set', verbose_name=_('Setor')
    )
    map_link = models.URLField(_('Link do Mapa'), blank=True, help_text=_('URL do Google Maps'))
    is_active = models.BooleanField(
        _('Ativo'), default=False, help_text=_('Marque esta opção para que o lugar fique disponivel')
    )
    n_computers = models.IntegerField(_('Número de Computadores'), validators=[MinValueValidator(0)], default=0)
    capacity = models.IntegerField(_('Capacidade de pessoas'), validators=[MinValueValidator(0)], default=0)
    is_air_conditioner = models.BooleanField(_('Ar Condicionado'), default=False)
    is_board = models.BooleanField(_('Quadro'), default=False)
    is_projector = models.BooleanField(_('Projetor'), default=False)
    is_internet = models.BooleanField(_('Internet'), default=False)
    is_soundbox = models.BooleanField(_('Caixa de Som'), default=False)
    is_washroom = models.BooleanField(_('Banheiro'), default=False)
    is_water = models.BooleanField(_('Bebedouro'), default=False)
    is_bleachers = models.BooleanField(_('Arquibancada'), default=False)
    is_roof = models.BooleanField(_('Cobertura'), default=False)
    type_court = models.CharField(
        _('Tipo de Quadra'), choices=TypeCourt.choices, default=TypeCourt.NO, null=True, max_length=2
    )

    class Meta:
        ordering = ['type']
        verbose_name = _('Espaço')
        verbose_name_plural = _('Espaços')

    def __str__(self):
        return f'{self.name} - {self.department}'

    @property
    def get_bg_color(self):
        if self.type.name.lower() == 'auditório':
            return 'bg-gradient-blue'
        elif self.type.name.lower() == 'laboratório':
            return 'bg-gradient-green'
        elif self.type.name.lower() == 'quadra':
            return 'bg-gradient-orange'
        else:
            return ''



