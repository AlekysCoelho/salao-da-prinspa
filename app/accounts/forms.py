from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from rolepermissions.roles import assign_role

User = get_user_model()

class UsersCreationForm(UserCreationForm):
    # Adicionando o campo 'role' diretamente ao formulário
    role = forms.ChoiceField(
        choices=[
            ('manager', 'Gerente'),
            ('receptionist', 'Recepcionista'),
        ],
        label='Função (Role)',
        required=True
    )
    class Meta:
        model = User
        fields = ("username", "email", "bio", "role") # Inclua o campo 'role' aqui

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    # Método para salvar o usuário e atribuir o role
    def save(self, commit=True):
        # Salva o usuário primeiro, sem o campo 'role'
        user = super().save(commit=False)
        user.save()

        # Atribui o role ao usuário recém-criado
        role_name = self.cleaned_data.get('role')
        if role_name:
            assign_role(user, role_name)
        
        return user


class UsersChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('bio',)