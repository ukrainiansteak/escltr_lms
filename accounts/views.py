from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import AccountRegisterForm
from accounts.models import Profile

from django.contrib.auth import get_user_model


user = get_user_model()


class AccountRegister(CreateView):
    model = Profile
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:index')
    form_class = AccountRegisterForm

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     messages.success(
    #         self.request,
    #         'Profile created successfully. You can now sign in.'
    #     )
    #     return result


class AccountLogin(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('accounts:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f'User {self.request.user.username} logged in successfully.'
        )
        return result


class MainPage(TemplateView):
    template_name = 'index.html'
