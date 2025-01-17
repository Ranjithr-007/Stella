from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'mobile', 'subject', 'query']