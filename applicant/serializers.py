""" For Django-Rest-Framework Serialization"""

from .models import Resume, Education, Experience
from rest_framework import serializers


# Serializers define the API representation
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = ('timestamp_updated', 'name', 'location')
