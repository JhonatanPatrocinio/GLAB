from django import forms
from django.contrib.auth import forms as f
from django.utils.translation import gettext_lazy as _


class MyAuthenticationForm(f.AuthenticationForm):
    username = f.UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'autofocus': True, 'placeholder': _('Email')})
    )
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': _('Password')}),
    )

