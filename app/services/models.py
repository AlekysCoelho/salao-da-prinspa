import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Service Name'), max_length=250, help_text='haircut or manicure')
    duration = models.DurationField(_('Duration of Service.'))
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('beauty_service')
        ordering = ['name']
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self) -> str:
        return f'{self.name}'