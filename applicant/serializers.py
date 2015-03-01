"""
    For Django-Rest-Framework Serialization
    http://www.django-rest-framework.org/api-guide/serializers/
    Serializers allow complex data (e.g. querysets and model instances)
    to be converted to native Python datatypes that can be easily rendered
    into JSON, XML or other types.  Serializers also provide deserialization,
    allowing parsed data to be converted back into complex types,
    after first validating the incoming data.
"""


from .models import Resume, Education, Experience
from rest_framework import serializers


# Serializers define the API representation
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = ('active', 'timestamp_updated', 'name', 'location',
                  'phone_number', 'accomplishment')


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('school', 'location', 'start_date', 'end_date', 'current',
                  'title', 'description')


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ('company', 'location', 'start_date', 'end_date', 'current',
                  'title', 'description')
