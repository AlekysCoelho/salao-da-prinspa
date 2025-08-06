from django.contrib import admin
from django.urls import include, path

from app.accounts.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('app.accounts.urls', namespace='accounts')),
    path('appointments/', include('app.appointment.urls', namespace='appointment')),
    path('clients/', include('app.client.urls', namespace='client')),
    path('professionals/', include('app.professional.urls', namespace='professional')),
    path('services/', include('app.service.urls', namespace='service')),
    path('reports/', include('app.reports.urls', namespace='reports')),
]