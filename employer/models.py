"""  Employers post jobs and company information here """
from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User  # Get User info


class Job(models.Model):
    """ Information about the job listing; what company, title, salary, description,
        picture of office, etc. """
    active = models.BooleanField(default=True, blank=False)
    created_by = models.ForeignKey(User)
    company = models.CharField(max_length=255, null=False, blank=True) # What company posted job
    timestamp_created = models.DateTimeField(auto_now=False,  # Update now
                                             auto_now_add=True  # When create
                                             )
    timestamp_updated = models.DateTimeField(auto_now=True,  # Update now
                                             auto_now_add=False  # When create
                                             )
    title = models.CharField(max_length=255, null=False, blank=True)  # Job Title
    description = models.TextField() # Description about the job

    # Types of jobs
    JOB_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contact', 'Contact'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
    )
    status = models.CharField(max_length=10,
                             choices=JOB_CHOICES)

    OCCUPATION_GROUP = (
        ('Accounting and Finance', 'Accounting and Finance'),
        ('Admin and Office', 'Admin and Office'),
        ('Architecture and Engineering', 'Architecture and Engineering'),
        ('Art, Media, and Design', 'Art, Media, and Design'),
        ('Biotech and Science', 'Biotech and Science'),
        ('Business and Management', 'Business and Management'),
        ('Customer Service', 'Customer Service'),
        ('Data and Information Systems', 'Data and Information Systems'),
        ('Education', 'Education'),
        ('Food, Beverage, and Hospitality', 'Food, Beverage, and Hospitality'),
        ('General Labor', 'General Labor'),
        ('Government', 'Government'),
        ('Human Resources', 'Human Resources'),
        ('Legal', 'Legal'),
        ('Manufacturing', 'Manufacturing'),
        ('Marketing, PR, and Advertising', 'Marketing, PR, and Advertising'),
        ('Medical and Health', 'Medical and Health'),
        ('Nonprofit', 'Nonprofit'),
        ('Programming', 'Programming'),
        ('Real Estate', 'Real Estate'),
        ('Retail and Wholesale', 'Retail and Wholesale'),
        ('Sales and Business Development', 'Sales and Business Development'),
        ('Salon, Spa, and Fitness', 'Salon, Spa, and Fitness'),
        ('Security', 'Security'),
        ('Skilled Trade and Craft', 'Skilled Trade and Craft'),
        ('Technical Support', 'Technical Support'),
        ('Transport', 'Transport'),
        ('TV, Film, and Video', 'TV, Film, and Video'),
        ('Writing and Editing', 'Writing and Editing'),
    )
    occupation = models.CharField(max_length=50,
                                  choices=OCCUPATION_GROUP,
                                  blank=True)

    salary_min = models.IntegerField(null=False, blank=True)
    salary_max = models.IntegerField(null=False, blank=True)

    #picture = models.ImageField(upload_to='images/jobs/')
    picture = models.FileField(upload_to='images/jobs/', blank=True)

    location = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        ordering = ['timestamp_created']  # Automatically order by latest first

    def __unicode__(self):
        return smart_unicode(self.title)  # Return identifer

    def get_active(self):
        if self.active:
            return True
        else:
            return False

