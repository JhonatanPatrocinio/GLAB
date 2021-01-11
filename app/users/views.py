from django.contrib.auth import views
from django.urls import reverse_lazy

from .forms import MyAuthenticationForm


class LoginView(views.LoginView):
    template_name = 'login/index.html'
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('')
