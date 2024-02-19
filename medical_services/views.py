from django.shortcuts import render
from medical_services.models import Medical_service


def index(request):
    # Получаем все медицинские услуги
    medical_services = Medical_service.objects.all()

    # Контекст для передачи данных в шаблон
    context = {
        'object_list': medical_services,
        'title': 'Главная'
    }

    # Рендерим главную страницу с передачей контекста
    return render(request, 'medical_services/index.html', context)


def services(request):
    # Получаем все медицинские услуги
    medical_services = Medical_service.objects.all()

    # Контекст для передачи данных в шаблон
    context = {
        'object_list': medical_services,
        'title': 'Наши услуги'
    }

    # Рендерим страницу с услугами с передачей контекста
    return render(request, 'medical_services/services.html', context)


def about_us(request):
    # Рендерим страницу "О нас"
    return render(request, 'medical_services/about_us.html')


def contacts(request):
    # Рендерим страницу с контактами
    return render(request, 'medical_services/contacts.html')


def service_detail(request, service_id):
    # Получаем конкретную медицинскую услугу по её идентификатору
    medical_service = Medical_service.objects.get(pk=service_id)

    # Рендерим страницу с деталями медицинской услуги
    return render(request, 'medical_services/service.html', {'medical_service': medical_service})


#def medical_consultation(request):
    # Рендерим страницу с медицинскими консультациями
#    return render(request, 'medical_services/medical_consultation.html')


def privacy_policy(request):
    # Рендерим страницу с политикой конфиденциальности
    return render(request, 'medical_services/privacy_policy.html')
