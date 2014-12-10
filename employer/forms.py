from django.contrib.auth.models import User
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job

        fields = ['company', 'title', 'description', 'salary_min', 'salary_max', 'occupation', 'status', 'picture', 'location']  # Explicitly list only these fields
