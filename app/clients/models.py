from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.model import BaseModel

User = get_user_model()

class Client(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=250)
    phone = models.CharField(_("Phone Number"), max_length=14, help_text='+55 85 999999999')
    email = models.EmailField(help_text='user@gmail.com')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    

    class Meta(BaseModel.Meta):
        db_table = _('beauty_client')
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        ordering = ('name',)

    def __str__(self) -> str:
        return f'{self.name}'
