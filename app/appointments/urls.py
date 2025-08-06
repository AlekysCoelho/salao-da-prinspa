from django.urls import path

from .views import AppointmentCreateView, MyAppointmentsView

app_name = 'appointment'

urlpatterns = [
    path('create/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('my-appointments/', MyAppointmentsView.as_view(), name='my_appointments'),
]