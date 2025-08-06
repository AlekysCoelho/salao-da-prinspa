from django.db import models
from django.utils.translation import gettext_lazy as _

from app.clients.models import Client
from app.professionals.models import Professional
from app.services.models import Service
from app.utils.model import BaseModel


class Appointment(BaseModel):
    STATUS_APPOINTMENT = (
        ('Canceled', _('Canceled')),
        ('Scheled', _('Scheduled')),
        ('Completed', _('Completed')),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    scheduled_at = models.DateTimeField(_("Scheduled Date & Time"))
    status = models.CharField(_("Scheduling Status"), max_length=9, choices=STATUS_APPOINTMENT)

    class Meta(BaseModel.Meta):
        db_table = _('beauty_appointments')
        ordering = ['scheduled_at', 'client', 'professional']
        unique_together = ('client', 'scheduled_at')
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    def __str__(self) -> str:
        return f'{self.client.name} - {self.professional.name} - {self.service.name}: {self.scheduled_at}'