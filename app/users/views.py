
from django.views.generic import FormView, CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth import views, get_user_model, mixins
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import MyAuthenticationForm, ChoiceUserForm, TeacherForm, UserForm, StudentForm, UserChangeForm


User = get_user_model()


class LoginView(views.LoginView):
    template_name = 'login/index.html'
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_page'] = True
        return context

    def get_success_url(self):
        type_user = self.request.user.get_type
        if type_user == 'T':
            return reverse_lazy('teacher:dashboard_teacher')
        elif type_user == 'S':
            return reverse_lazy('students:dashboard_student')
        else:
            return reverse_lazy('admin:index')


class LogoutView(mixins.LoginRequiredMixin, views.LogoutView):
    template_name = 'login/index.html'


class ChoiceSignUpView(FormView):
    template_name = 'signup/cadastro_escolha.html'
    form_class = ChoiceUserForm

    def form_valid(self, form):
        if int(form.cleaned_data['choice']) == 0:
            return redirect('signup:teacher_signup')
        elif int(form.cleaned_data['choice']) == 1:
            return redirect('signup:student_signup')
        else:
            return self.render_to_response(self.get_context_data())


class TeacherSignUpView(CreateView):
    template_name = 'signup/cadastro_docente.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    model = User

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_teacher = TeacherForm()

        return self.render_to_response(self.get_context_data(form=form, form_teacher=form_teacher))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_teacher = TeacherForm(request.POST)
        if form.is_valid() and form_teacher.is_valid():
            return self.form_valid(form, form_teacher)
        else:
            return self.form_invalid(form, form_teacher)

    def form_valid(self, form, form_teacher):
        self.object = form.save()
        form_teacher.save(user=self.object)
        messages.success(self.request, 'Docente criado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_teacher):
        return self.render_to_response(self.get_context_data(form=form, form_teacher=form_teacher))


class StudentSignUpView(CreateView):
    template_name = 'signup/cadastro_discente.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    model = User

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_student = StudentForm()

        return self.render_to_response(self.get_context_data(form=form, form_student=form_student))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        form_student = StudentForm(request.POST)
        if form.is_valid() and form_student.is_valid():
            return self.form_valid(form, form_student)
        else:
            return self.form_invalid(form, form_student)

    def form_valid(self, form, form_student):
        self.object = form.save()
        form_student.save(user=self.object)
        messages.success(self.request, 'Discente criado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_student):
        return self.render_to_response(self.get_context_data(form=form, form_student=form_student))


class StudentEditProfileView(mixins.LoginRequiredMixin, UpdateView):
    template_name = 'editar_discente.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('students:dashboard_student')
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_student = StudentForm(instance=self.object.student_set.all().first())

        return self.render_to_response(self.get_context_data(form=form, form_student=form_student))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_student = StudentForm(request.POST, instance=self.object.student_set.all().first())
        if form.is_valid() and form_student.is_valid():
            return self.form_valid(form, form_student)
        else:
            return self.form_invalid(form, form_student)

    def form_valid(self, form, form_student):
        self.object = form.save()
        form_student.save(user=self.object)
        messages.success(self.request, 'Discente atualizado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_student):
        return self.render_to_response(self.get_context_data(form=form, form_student=form_student))


class TeacherEditProfileView(UpdateView):
    template_name = 'editar_docente.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('login')
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_teacher = TeacherForm(instance=self.object.teacher_set.all().first())

        return self.render_to_response(self.get_context_data(form=form, form_teacher=form_teacher))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        form_teacher = TeacherForm(request.POST, instance=self.object.teacher_set.all().first())
        if form.is_valid() and form_teacher.is_valid():
            return self.form_valid(form, form_teacher)
        else:
            return self.form_invalid(form, form_teacher)

    def form_valid(self, form, form_teacher):
        self.object = form.save()
        form_teacher.save(user=self.object)
        messages.success(self.request, 'Docente atualizado com sucesso')
        return redirect(self.get_success_url())

    def form_invalid(self, form, form_teacher):
        return self.render_to_response(self.get_context_data(form=form, form_teacher=form_teacher))

