from django.urls import path
from feedback.views import feedback_view

app_name = 'feedback'

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('feedback/', feedback_view, name='feedback'),

]

