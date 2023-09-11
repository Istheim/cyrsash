from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from dispatches.apps import DispatchesConfig
from dispatches.views import base, home

app_name = DispatchesConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('home/', home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)