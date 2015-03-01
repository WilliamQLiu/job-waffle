from django.contrib.auth.models import User
from django import forms
from .models import Resume, Education, Experience


"""
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        #exclude = ('username',)
        fields = ['name', 'location', 'phone_number', 'accomplishment']  # Explicitly list only these fields
"""


class ResumeForm(forms.Form):
    name = forms.CharField(label='name', max_length=512)
    location = forms.CharField(label='Location')
    phone_number = forms.CharField(label='Phone Number', max_length=11)
    accomplishment = forms.CharField()
