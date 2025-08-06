import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from app.services.models import Service


class Professional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Profissional Name'), max_length=250)
    services = models.ManyToManyField(Service, related_name='professionals')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('beauty_professional')
        ordering = ['name']
        verbose_name = _('Professional')
        verbose_name_plural = _('Professionals')

    def __str__(self) -> str:
        return f'{self.name}'
    

class Availability(models.Model):
    WEEKDAY_CHOICES = (
        ('monday', _('Monday')),
        ('tuesday', _('Tuesday')),
        ('wednesday', _('Wednesday')),
        ('rhursday', _('Thursday')),
        ('friday', _('Friday')),
        ('saturday', _('Saturday')),
        ('sunday', _('Sunday')),
    )

    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='availabities'
    )
    weekday = models.CharField(_('Weekday'), max_length=10, choices=WEEKDAY_CHOICES)
    start_time = models.TimeField(_('Start time'))
    end_time = models.TimeField(_('End Time'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('beauty_availability')
        ordering = ['professional', 'weekday', 'start_time']
        unique_together = ('professional', 'weekday', 'start_time')
        verbose_name = _('Availability')
        verbose_name_plural = _('Availabilities')

    def __str__(self) -> str:
        message = (
            f"{self.professional.name} - {self.get_weekday_display()}:" # type: ignore
            f"{self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"
        )
        return  message