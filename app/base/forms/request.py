from django import forms
from django.contrib.auth import get_user_model

from base.models import Requester


User = get_user_model()


class RequesterForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Requester
        fields = ('user', 'department', 'registry')
        widgets = {
            'registry': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput()
        }

    def save(self, commit=True, user=None):
        self.instance.user = user
        return super().save(commit)
