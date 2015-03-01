"""  Employers post jobs """
from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User  # Get User info


class Job(models.Model):
    """
        Information about the job post:
        Company, title, salary, description, picture of office, etc
    """
    active = models.BooleanField(default=True, blank=False)
    created_by = models.ForeignKey(User)
    company = models.CharField(max_length=512, null=False, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    timestamp_created = models.DateTimeField(auto_now=False,  # Update now
                                             auto_now_add=True  # When create
                                             )
    timestamp_updated = models.DateTimeField(auto_now=True,  # Update now
                                             auto_now_add=True  # When create
                                             )
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField()  # Description about the job
    status = models.CharField(max_length=10)
    salary_min = models.IntegerField(null=False, blank=True)
    salary_max = models.IntegerField(null=False, blank=True)

    picture = models.FileField(upload_to='images/jobs/', blank=True)

    class Meta:
        ordering = ['timestamp_created']  # Automatically order by latest first

    def __unicode__(self):
        return smart_unicode(self.title)  # Return identifer

    def get_active(self):
        if self.active:
            return True
        else:
            return False
