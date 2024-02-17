from django.shortcuts import render
from medical_services.models import Medical_service

def index(request):
    context = {
        'object_list': Medical_service.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'medical_services/index.html', context)


def services(request):
    context = {
        'object_list': Medical_service.objects.all(),
        'title': 'Наши услуги'
    }
    return render(request, 'medical_services/services.html', context)