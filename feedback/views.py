from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()

            # Добавляем сообщение об успешной отправке формы
            messages.success(request, 'Ваше сообщение успешно отправлено.')

            # Перенаправляем пользователя на ту же страницу
            return redirect('feedback:feedback')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})
