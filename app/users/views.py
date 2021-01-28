
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from django.contrib.auth import views, get_user_model, mixins
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.utils.translation import ugettext_lazy as _


from .forms import MyAuthenticationForm, UserForm, UserChangeForm, ChangePassword
from base.forms import RequesterForm


User = get_user_model()


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
        if request.POST.get('username', None):
            try:
                user = User.objects.get(email=request.POST.get('username', None))
                if not user.is_active:
                    messages.error(request, 'Usuário inativo, contate o administrador do sistema')
                    return redirect('login')
                return super(LoginView, self).post(request, *args, **kwargs)
            except User.DoesNotExist:
                return super(LoginView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        if not self.request.user.is_staff:
            return reverse_lazy('dashboard')
        else:
            return reverse_lazy('admin:index')


class LogoutView(mixins.LoginRequiredMixin, views.LogoutView):
    template_name = 'accounts/login.html'


class SignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    model = User

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_requester = RequesterForm()
        return self.render_to_response(self.get_context_data(form=form, form_requester=form_requester))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_requester = RequesterForm(request.POST)
        if form.is_valid() and form_requester.is_valid():
            return self.form_valid(form, form_requester)
        else:
            return self.form_invalid(form, form_requester)

    def form_valid(self, form, form_requester):
        self.object = form.save()
        form_requester.save(user=self.object)
        messages.success(self.request, 'Usuário criado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_requester):
        return self.render_to_response(self.get_context_data(form=form, form_requester=form_requester))


class DetailProfileView(DetailView):
    template_name = 'accounts/detail_profile.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).prefetch_related('requester_set')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("User not found"))
        return obj


class EditProfileView(mixins.LoginRequiredMixin, UpdateView):
    template_name = 'accounts/edit_profile.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile:detail_profile')
    model = User

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).prefetch_related('requester_set')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("User not found"))
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_requester = RequesterForm(instance=self.object.requester_set)

        return self.render_to_response(self.get_context_data(form=form, form_requester=form_requester))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_requester = RequesterForm(request.POST, instance=self.object.requester_set)
        if form.is_valid() and form_requester.is_valid():
            return self.form_valid(form, form_requester)
        else:
            return self.form_invalid(form, form_requester)

    def form_valid(self, form, form_requester):
        self.object = form.save()
        form_requester.save(user=self.object)
        messages.success(self.request, 'Cadastro atualizado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_requester):
        return self.render_to_response(self.get_context_data(form=form, form_requester=form_requester))


class ChangePasswordView(views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    form_class = ChangePassword


    def get_success_url(self):
        messages.success(self.request, 'Senha atualizada com sucesso')
        return reverse_lazy('profile:detail_profile')


