from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from medical_services.views import index

urlpatterns = [
    path('', index),
]

