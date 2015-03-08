"""
    Using Haystack to connect to Elasticsearch so we can search on indexes
"""


from haystack import indexes
from .models import Job


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    """
        Search through job indexes; every SearchIndex requires only one field
        with 'document=True' to indicate this is the primary field to search
        Convention is to name this field 'text'
    """
    text = indexes.CharField(document=True, use_template=True)
    company = indexes.CharField(model_attr='company')
    location = indexes.CharField(model_attr='location')
    title = indexes.CharField(model_attr='title')
    status = indexes.CharField(model_attr='status')
    description = indexes.CharField(model_attr='description')
    salary_min = indexes.IntegerField(model_attr='salary_min')
    salary_max = indexes.IntegerField(model_attr='salary_max')

    def get_model(self):
        return Job

    def index_queryset(self, using=None):
        """ Used when entire index for model is updated """
        return self.get_model().objects
