from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, TemplateView

from accounts.forms import AccountRegisterForm, UserEditForm, TeacherProfileEditForm, StudentProfileEditForm
from accounts.models import Profile

from django.contrib.auth import get_user_model


user = get_user_model()


class AccountRegister(CreateView):
    model = Profile
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:index')
    form_class = AccountRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            'Profile created successfully. You can now sign in.'
        )
        return result


class AccountLogin(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('accounts:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f'User {self.request.user.first_name} logged in successfully.'
        )
        return result


class MainPage(TemplateView):
    template_name = 'index.html'


class AccountEdit(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_form = UserEditForm(instance=user)

        context = dict()
        context['user_form'] = user_form

        if user.teacher:
            teacher_form = TeacherProfileEditForm()
            context['teacher_form'] = teacher_form
        elif user.student:
            student_form = StudentProfileEditForm()
            context['student_form'] = student_form

        return render(
            request,
            'profile.html',
            context,
        )

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = UserEditForm(
            instance=user,
            data=request.POST,
            files=request.FILES
        )

        if user_form.is_valid():
            user_form.save()
            messages.success(
                request,
                'Profile updated successfully.'
            )
            return redirect(reverse('accounts:profile'))

        return render(
            request,
            'profile.html',
            context={
                'user_form': user_form,
            }
        )

    def put(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            'Password updated successfully.'
        )
        return result
