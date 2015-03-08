"""
    Forms accept input from users, processes that data, and responds.  Specify
      *  where the URL the data should be returned (form's <action> attribute)
      *  how the HTTP method should be returned (GET or POST)

    Form maps to HTML form <input> elments similar to how Django's Model
    maps to a database field
    Forms return 'myform.is_valid()' (True or False) if all fields are valid
    Forms return 'myform.errors', which is a dict of errors (if any)

    Intro Tutorial: https://docs.djangoproject.com/en/1.7/topics/forms/
    Core Form Concepts: http://www.pydanny.com/core-concepts-django-forms.html
    Core ModelForm Concepts: http://www.pydanny.com/core-concepts-django-modelforms.html
    # ModelForm is a helper class to Form ()

"""

from django import forms
from django.contrib.admin import widgets
from haystack.forms import SearchForm
#from .models import Job


"""
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # Explicitly list only these fields:
        fields = ['company', 'location', 'title', 'description', 'status',
                  'salary_min', 'salary_max', 'picture']
"""

JOB_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
)      # Types of jobs


class JobForm(forms.Form):
    company = forms.CharField(label='Company', max_length=512)
    location = forms.CharField(label='Location')
    title = forms.CharField(label='Job Title')
    description = forms.CharField(label='Job Description')
    status = forms.ChoiceField(required=False, choices=JOB_CHOICES)
    salary_min = forms.IntegerField()
    salary_max = forms.IntegerField()
    picture = forms.Field(label='Image', widget=forms.FileInput,
                          required=False)


class JobSearchForm(SearchForm):
    """ Haystack Form for searching specific jobs by desc and location """
    active = forms.BooleanField(label='active')
    timestamp_created = forms.DateTimeField(label='timestamp_created')
    main = forms.CharField(label='Main')
    company = forms.CharField(label='Company', max_length=512)
    location = forms.CharField(label='Location')
    title = forms.CharField(label='Job Title')
    description = forms.CharField(label='Job Description')
    status = forms.ChoiceField(required=False, choices=JOB_CHOICES)
    salary_min = forms.IntegerField()
    salary_max = forms.IntegerField()
    location = forms.CharField(label='Location')


    def search(self):
        sqs = super(JobSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        return sqs  # returns the SearchQuerySet

    def no_query_found(self):
        return self.searchqueryset.all()
