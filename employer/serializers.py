"""
    For Django-Rest-Framework Serialization
    http://www.django-rest-framework.org/api-guide/serializers/
    Serializers allow complex data (e.g. querysets and model instances)
    to be converted to native Python datatypes that can be easily rendered
    into JSON, XML or other types.  Serializers also provide deserialization,
    allowing parsed data to be converted back into complex types,
    after first validating the incoming data.

    For testing, we have jobs here
    http://localhost:8000/api/job/?format=json
"""


from .models import Job
from rest_framework import serializers


# Serializers define the API representation
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('company', 'title', 'description', 'status',
                  'occupation', 'salary_min', 'salary_max', 'location')
