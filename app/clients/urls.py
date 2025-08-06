from django.urls import path

from .views import ClientRegistrationView

app_name = 'client'

urlpatterns = [
    path('register/', ClientRegistrationView.as_view(), name='client_register'),
]