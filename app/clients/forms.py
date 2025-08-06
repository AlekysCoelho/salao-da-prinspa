from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Client

User = get_user_model()

class ClientRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=Client.GENDER_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Client.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                phone=self.cleaned_data['phone'],
                gender=self.cleaned_data['gender'],
            )
        return user