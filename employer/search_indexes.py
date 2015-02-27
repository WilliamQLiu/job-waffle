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

    def get_model(self):
        return Job
