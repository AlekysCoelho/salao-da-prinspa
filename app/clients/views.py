from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ClientRegistrationForm


class ClientRegistrationView(SuccessMessageMixin, CreateView):
    form_class = ClientRegistrationForm
    template_name = 'clients/register.html'
    success_url = reverse_lazy('accounts:login')
    success_message = 'Cadastro realizado com sucesso! Você já pode fazer login.'
