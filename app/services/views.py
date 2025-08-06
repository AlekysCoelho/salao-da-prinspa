from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rolepermissions.mixins import HasRoleMixin

from .forms import ServiceForm
from .models import Service


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'services'


class ServiceCreateView(LoginRequiredMixin, HasRoleMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/service_create.html'
    success_url = reverse_lazy('service:list')
    allowed_roles = ['manager']  # Apenas gerentes podem criar serviços

    def form_valid(self, form):
        messages.success(self.request, 'Serviço criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar serviço. Verifique os dados informados.')
        return super().form_invalid(form)