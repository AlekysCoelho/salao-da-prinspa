from django.urls import path

from .views import ServiceCreateView, ServiceListView

app_name = 'services'

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('create_service/', ServiceCreateView.as_view(), name='create_service'),
]