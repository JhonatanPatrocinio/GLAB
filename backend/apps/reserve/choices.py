from django.utils.translation import gettext_lazy as _


RESPONSE_WAITING = '1'
RESPONSE_DENIED = '2'
RESPONSE_ACCEPTED = '3'
UTILIZED = '4'
STATUS_RESERVE_CHOICES = [
    (RESPONSE_WAITING, _('Aguardando Resposta')),
    (RESPONSE_DENIED, _('Utilização Negada')),
    (RESPONSE_ACCEPTED, _('Utilização Aceita')),
    (UTILIZED, _('Utilizado'))
]
