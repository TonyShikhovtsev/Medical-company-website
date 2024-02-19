from django import forms
from feedback.models import FeedbackMessage

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ['name', 'phone', 'message']
