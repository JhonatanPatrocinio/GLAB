from django import forms
from django.contrib.auth import forms as f
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, forms as auth_forms, password_validation

from .models import Teacher, Student


User = get_user_model()


class MyAuthenticationForm(f.AuthenticationForm):
    username = f.UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'autofocus': True, 'placeholder': _('Email')})
    )
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': _('Password')}),
    )


class ChoiceUserForm(forms.Form):
    choice = forms.ChoiceField(
        choices=[(0, _('Professor')), (1, _('Aluno'))], widget=forms.HiddenInput()
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


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', )
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = ('registry', 'academic_center', 'user')
        widgets = {
            'registry': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_center': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput()
        }

    def save(self, commit=True, user=None):
        self.instance.user = user
        return super().save(commit)


class StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Student
        fields = ('registry', 'course', 'user')
        widgets = {
            'registry': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput()
        }

    def save(self, commit=True, user=None):
        self.instance.user = user
        return super().save(commit)

