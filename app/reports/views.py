# reports/views.py

from celery.result import AsyncResult
from django.shortcuts import render
from rolepermissions.decorators import has_role_decorator

from .forms import ReportForm
from .tasks import generate_report


@has_role_decorator('manager')
def report_view(request):
    form = ReportForm()
    report_result = None
    task_id = request.GET.get("task_id")

    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            task = generate_report.delay(
                form.cleaned_data["start_date"].strftime("%Y-%m-%d"),
                form.cleaned_data["end_date"].strftime("%Y-%m-%d")
            )
            return render(request, "reports/report_pending.html", {"task_id": task.id})

    if task_id:
        result = AsyncResult(task_id)
        if result.ready():
            report_result = result.result

    return render(request, "reports/report.html", {"form": form, "report_result": report_result})
