from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET
from rolepermissions.checkers import has_role

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        
        # Verifica se o usuário tem as permissões necessárias
        if has_role(user, ['receptionist', 'manager']):
            return super().form_valid(form)
        
        # Se não tiver as permissões, exibe mensagem de erro
        messages.error(
            self.request,
            'Acesso negado. Apenas recepcionistas e gerentes podem acessar o sistema.',
            extra_tags='danger'
        )
        return self.form_invalid(form)


def register_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        pass

@require_GET
def check_username(request):
    username = request.GET.get('username', '').strip()
    exists = User.objects.filter(username=username)
    html = render_to_string('partials/username_check_result.html', {'exists': exists})
    return html


def logout_view(request):
    auth.logout(request)
    return redirect("/accounts/login")
