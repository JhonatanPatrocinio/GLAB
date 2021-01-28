from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

from base.models import Reservation, Place


User = get_user_model()


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        super().__init__(format='%Y-%m-%d', **kwargs)


class ReservationForm(forms.ModelForm):
    user = forms.ModelChoiceField(required=False, queryset=User.objects.all())
    place = forms.ModelChoiceField(required=False, queryset=Place.objects.all())

    class Meta:
        model = Reservation
        fields = ('user', 'place', 'date', 'initial_time', 'end_time', 'reason', 'obs', 'phone')
        widgets = {
            'user': forms.HiddenInput(),
            'place': forms.HiddenInput(),
            'date': DateInput(attrs={'class': 'form-control'}),
            'initial_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control telefone'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError('O dia precisa ser igual ou maior que hoje')
        return date

    def clean(self):
        end_time = self.cleaned_data['end_time']
        if self.cleaned_data['initial_time'] > end_time:
            raise forms.ValidationError({'initial_time': 'O horário de inicio precisa ser menor que o fim'})
        return super().clean()

    def save(self, commit=True, user=None, place=None):
        if user:
            self.instance.user = user
        if place:
            self.instance.place = place
        return super().save(commit)
