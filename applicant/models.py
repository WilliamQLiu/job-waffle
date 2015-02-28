""" Job applicants post resume """
from django.contrib.auth.models import User  # Get User info
from django.db import models
from django.utils.encoding import smart_unicode

#from allauth.account.models import EmailAddress
#from allauth.socialaccount.models import SocialAccount

'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    about_me = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "http://www.gravatar.com/avatar/{}?s=40".format(
            hashlib.md5(self.user.email).hexdigest())

    def account_verified(self):
        """
        If the user is logged in and has verified hisser email address, return True,
        otherwise return False
        """
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
'''


class ResumeQuerySet(models.query.QuerySet):
    def get_active(self):
        return self.get_active(active=True)


class ResumeManager(models.Manager):
    """ Get specific views back """

    def get_active(self):
        """ Returns only active resumes, e.g. Resume.objects.get_active() """
        return super(ResumeManager, self).filter(active=True)


class Resume(models.Model):
    """ Applicant's Resume """
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True, blank=False)
    timestamp_created = models.DateTimeField(auto_now=False,  # Update now
                                             auto_now_add=True  # When create
                                             )
    timestamp_updated = models.DateTimeField(auto_now=True,  # Update now
                                             auto_now_add=False  # When create
                                             )
    name = models.CharField(max_length=255, null=False, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=11, null=False, blank=True)
    accomplishment = models.TextField()

    class Meta:
        ordering = ['timestamp_updated']  # Automatically order by latest first

    def __unicode__(self):
        return smart_unicode(self.name)  # Return identifer

    objects = ResumeManager()  # Link to ResumeManager


class Education(models.Model):
    """ Applicant's Education """
    resume = models.ForeignKey(Resume)
    school = models.CharField(max_length=1024, null=False, blank=True)
    location = models.CharField(max_length=512, null=False, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False, blank=False)
    title = models.CharField(max_length=1024, null=False, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['start_date']  # Automatically order by latest first

    def __unicode__(self):
        return smart_unicode(self.school)  # Return identifer


class Experience(models.Model):
    """ Applicant's Work or Volunteer Experience """
    resume = models.ForeignKey(Resume)
    company = models.CharField(max_length=512, null=False, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False, blank=False)  # Current at job
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['start_date']  # Automatically order by latest first

    def __unicode__(self):
        return smart_unicode(self.company)  # Return identifer


class Describe(models.Model):
    """ Describe your job """
    quesiton_1 = models.TextField("What was your biggested accomplishment?")
    question_2 = models.TextField("What was your average day like?")
    question_3 = models.TextField("What do you need to do your job?")
    question_4 = models.TextField("What do you like and dislike?")
    question_5 = models.TextField("What advice do you have for others looking to get into this field?")
