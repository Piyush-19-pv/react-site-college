from django import forms
from .models import Contact
from .models import Feedback

# app_name/forms.py

from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'father_name', 'phone_number', 'whatsapp_number', 'email', 'address', 'course']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_number']






class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'message', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
