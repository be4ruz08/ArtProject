from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, TemplateView, RedirectView
from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(self.success_url)


class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
