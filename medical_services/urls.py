from django.urls import path
from .views import index, services, about_us, contacts, service, medical_consultation, privacy_policy

app_name = 'medical_services'

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('service/', service, name='service'),
    path('medical_consultation/', medical_consultation, name='medical_consultation'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
]
