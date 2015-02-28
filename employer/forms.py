#from django.contrib.auth.models import User
from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # Explicitly list only these fields:
        fields = ['company', 'location', 'title', 'description', 'status',
                  'salary_min', 'salary_max', 'picture']
