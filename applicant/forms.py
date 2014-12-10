from django.contrib.auth.models import User
from django import forms
from .models import Resume, Education, Experience

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        #exclude = ('username',)
        fields = ['name', 'location', 'phone_number', 'accomplishment']  # Explicitly list only these fields
