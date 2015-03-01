from django.conf.urls import patterns, include, url
from django.conf import settings  # Need for static content
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework import routers


from applicant.views import base_page, ResumeCreateView, ResumeListView, \
    ResumeUpdateView, ResumeDeleteView, Profile
from employer.views import JobListView, \
    JobUpdateView, JobDeleteView
from employer.views import find_job, post_job

from applicant.views import ResumeViewSet, EducationViewSet, ExperienceViewSet
from employer.views import JobViewSet, manage_job_posts

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'api/resume', ResumeViewSet)
router.register(r'api/education', EducationViewSet)
router.register(r'api/experience', ExperienceViewSet)
router.register(r'api/job', JobViewSet)

urlpatterns = patterns('',

    # Examples:
    #url(r'^$', 'jobwaffle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", base_page, name="base"),  # Home Page

    ###### SOCIAL REGISTRATION with django-allauth
    # prevent extra are you sure logout step
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

    url(r"^accounts/", include("allauth.urls")),  # django-allauth

    ###### RESUMES

    # Create Resume
    url(r"^resume_create$", ResumeCreateView.as_view(), name="resume-create"),

    # List Specific Resume
    url(r'^profile/(?P<username>[-\w\d]+)/(?P<pk>\d+)/$',
        ResumeListView.as_view(), name="resume-list"),

    # Update Specific Resume
    url(r'^profile/(?P<username>\w+)/update/(?P<pk>\d+)/$',
        ResumeUpdateView.as_view(), name="resume-update"),

    # Delete Specific Resume
    url(r'^profile/(?P<username>\w+)/delete/(?P<pk>\d+)/$',
        ResumeDeleteView.as_view(), name="resume-delete"),

    #url(r"^resume_view$", .as_view() , name="resume-view"),

    ###### JOBS

    url(r"^find_job$", find_job, name="find_job"),  # Home Page

    # Job Listing Page
    url(r"^job_all$", JobListView.as_view(), name="job-all"),

    # Create Job post
    url(r"^post_job$", post_job, name="post_job"),  # Home Page
    #url(r"^job_create$", JobCreateView.as_view(), name="job-create"),  # Remove this class later

    # List all your job posts
    url(r'^manage_job_posts$', manage_job_posts, name='manage_job_posts'),

    # List Specific Job
    url(r'^job/list/(?P<pk>\d+)/$', JobListView.as_view(), name='job-list'),

    # Update Specific Job
    url(r'^job/update/(?P<pk>\d+)/$', JobUpdateView.as_view(), name='job-update'),

    # Delete Specific Job
    url(r'^job/delete/(?P<pk>\d+)/$', JobDeleteView.as_view(), name='job-delete'),


    # STATIC and MEDIA paths
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    # User Profile Page
    url(r'^profile/(?P<username>\w+)/$', Profile.as_view(),
        name="profile"),  # Profile Page

    # Django Rest Framework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Haystack for ElasticSearch, it's a URLconf point to 'SearchView' instance
    (r'^search/', include('haystack.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
