from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import index, services, about_us, contacts, service_detail, medical_consultation, privacy_policy
from django.views.decorators.cache import cache_page

app_name = 'medical_services'

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
   # path('service/<int:pk>/', cache_page(60)(service), name='service'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('medical_consultation/', medical_consultation, name='medical_consultation'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)