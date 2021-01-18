from django import forms
from django.contrib.auth import get_user_model

from base.models import Reservation


User = get_user_model()


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        super().__init__(format='%Y-%m-%d', **kwargs)


class ReservationForm(forms.ModelForm):
    user = forms.ModelChoiceField(required=False, queryset=User.objects.all())

    class Meta:
        model = Reservation
        fields = ('user', 'laboratory', 'date', 'initial_time', 'end_time', 'reason', 'obs')
        widgets = {
            'user': forms.HiddenInput(),
            'laboratory': forms.Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'initial_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control'})

        }




