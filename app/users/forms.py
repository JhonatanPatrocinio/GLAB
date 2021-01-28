from django import forms
from django.contrib.auth import forms as f
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, forms as auth_forms


User = get_user_model()


class MyAuthenticationForm(f.AuthenticationForm):
    username = f.UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'autofocus': True, 'placeholder': _('Email')})
    )
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': _('Password')}),
    )


class UserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('email', 'full_name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        obj = super(UserForm, self).save(False)
        obj.is_active = False
        if commit:
            obj.save()
        return obj


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('full_name', )
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangePassword(auth_forms.PasswordChangeForm):

    error_messages = {
        **auth_forms.PasswordChangeForm.error_messages,
        'password_incorrect': _("Senha atual incorreta"),
    }

    old_password = forms.CharField(
        label=_("Senha Atual"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True}),
    )

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        strip=False
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
    )
