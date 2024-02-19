from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Medical_service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование услуги')
    short_name = models.CharField(max_length=50, verbose_name='Скоращенное наименование услуги')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(verbose_name='изображение (превью)', upload_to='media/', **NULLABLE)
    price = models.IntegerField(**NULLABLE, verbose_name='Стоимость')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

