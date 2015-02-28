from __future__ import absolute_import
#from django.http import HttpResponseRedirect, HttpResponse
# login_required decorator
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.decorators import method_decorator  # Allow LoggedInMixin
from django.views.generic import TemplateView, View, ListView, \
    UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.models import User
import django_filters

from .models import Resume, Education, Experience
from .forms import ResumeForm
from .serializers import ResumeSerializer, EducationSerializer, \
    ExperienceSerializer

from rest_framework import viewsets, authentication, permissions, filters


class LoggedInMixin(object):
    """ Mixin to ensure user is logged in """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

    #paginate_by = 50
    #paginate_by_param = 'page_size'
    #max_paginate_by = 500


class Base(ListView):
    """ Show User Profile, list advice """
    #model = Advice
    template_name = "base.html"

    def get_success_url(self):
        return reverse('base')

    def get_queryset(self):
        """ Get just logged in user's data """
        #return Advice.objects.filter(user_id=self.request.user)
        return Resume.objects.all()


class Profile(LoggedInMixin, ListView):
    """ Show User Profile, list resumes """
    model = Resume
    template_name = "profile.html"

    def get_success_url(self):
        return reverse('profile')

    def get_queryset(self):
        """ Get just logged in user's data """
        return Resume.objects.filter(user_id=self.request.user)


class ResumeCreateView(LoggedInMixin, FormView):
    """ Allow Users to Create Resumes """
    form_class = ResumeForm
    template_name = "resume_create.html"

    def get_success_url(self):
        """ After creating resume, takes you back to profile """
        name = self.request.user.username
        return reverse('profile', args=[name])

    def get_context_data(self, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('resume-create')
        return context

    def form_valid(self, form):
        # Say this is the default user
        form.instance.user = self.request.user
        context = form.save()
        return super(ResumeCreateView, self).form_valid(form)


class ResumeListView(LoggedInMixin, ListView):
    """ View a specific resume """
    model = Resume
    template_name = "resume_view.html"

    # Testing out celery
    #hello_tasks()  # Run immediately
    #hello_tasks.delay()  # Run using redis
    #multiply(5)

    def get_success_url(self):
        return reverse('resume-list')

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Resume.objects.filter(id=specific_id)


class ResumeUpdateView(LoggedInMixin, UpdateView):
    """ Update a specific resume """
    model = Resume
    #template_name_suffix = '_update_form'
    template_name = "resume_update.html"

    def get_success_url(self):
        """ After updating a resume, takes you back to profile """
        name = self.request.user.username
        return reverse('profile', args=[name])

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Resume.objects.filter(id=specific_id)


class ResumeDeleteView(LoggedInMixin, DeleteView):
    """ Delete a specific resume """
    model = Resume
    template_name = "resume_delete.html"

    def get_success_url(self):
        """ After deleting a resume, takes you back to profile """
        name = self.request.user.username
        return reverse('profile', args=[name])


'''
class ResumeFilter(django_filters.FilterSet):
    # list fields to filter by

    class Meta:
        model = Resume
        # list fields


class ResumeViewSet(LoggedInMixin, viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    filter_class = ResumeFilter
'''

# FOR DJANGO REST FRAMEWORK (DRF)

class DefaultsMixin(object):
    """
        Default settings for view authentication, permissions,
        filtering and pagination
    """
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
        )

    permission_classes = (
        permissions.IsAuthenticated,  # Access to GET, POST, HEAD, OPTIONS
        #IsReadOnlyRequest,
        #permissions.IsAuthenticatedOrReadOnly
        )

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        )

    paginate_by = 50
    paginate_by_param = 'page_size'
    max_paginate_by = 500


# DRF FILTERS

class ResumeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name')

    class Meta:
        model = Resume
        fields = ('timestamp_updated', 'name', 'location')


class EducationFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(name='start_date',
                                           lookup_type='gte')
    end_date = django_filters.DateFilter(name='end_date', lookup_type='lte')

    class Meta:
        model = Education
        fields = ('school', 'location', 'start_date', 'end_date', 'current',
                  'title', 'description')


class ExperienceFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(name='start_date',
                                           lookup_type='gte')
    end_date = django_filters.DateFilter(name='end_date', lookup_type='lte')

    class Meta:
        model = Experience
        fields = ('company', 'location', 'start_date', 'end_date', 'current',
                  'title', 'description')


# DRF VIEWSETS

class ResumeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_class = ResumeFilter
    search_fields = ('name')
    ordering_fields = ('timestamp_updated')


class EducationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_class = EducationFilter
    search_fields = ('start_date', 'end_date')


class ExperienceViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_class = ExperienceFilter
    search_fields = ('start_date', 'end_date')

