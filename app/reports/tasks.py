from datetime import datetime

from celery import shared_task
from django.utils.timezone import make_aware

from app.appointments.models import Appointment


@shared_task
def generate_report(start_date: str, end_date: str):
    start = make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
    end = make_aware(datetime.strptime(end_date, "%Y-%m-%d"))

    total = Appointment.objects.filter(
        status="completed",
        date__range=(start, end)
    ).count()

    return total