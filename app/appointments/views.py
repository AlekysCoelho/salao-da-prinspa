from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import AppointmentForm
from .models import Appointment


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/create_appointment.html'
    success_url = reverse_lazy('appointment:my_appointments')

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.status = 'Scheduled'
        messages.success(self.request, 'Agendamento realizado com sucesso!')
        return super().form_valid(form)

class MyAppointmentsView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/my_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user.client)