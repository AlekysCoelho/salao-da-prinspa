from django.urls import path

from .views import CustomLoginView, check_username, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check_username'),
]