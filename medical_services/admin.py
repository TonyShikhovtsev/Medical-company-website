from django.contrib import admin
from medical_services.models import Medical_service

@admin.register(Medical_service)
class Medical_serviceadmin(admin.ModelAdmin):
    list_display = ('name', 'short_name',  'description', 'image', 'price')
    list_filter = ('name', 'price')

