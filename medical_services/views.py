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


def about_us(request):
    return render(request, 'medical_services/about_us.html')


def contacts(request):
    return render(request, 'medical_services/contacts.html')

def service(request):
    return render(request, 'medical_services/service.html')

def medical_consultation(request):
    return render(request, 'medical_services/medical_consultation.html')

def privacy_policy(request):
    return render(request, 'medical_services/privacy_policy.html')