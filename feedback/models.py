from django.db import models
from django.contrib.auth.models import User

class FeedbackMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратной связи'