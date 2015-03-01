"""
    A view takes a web request and returns a web response
    The response can be a web page, a redirect, a 404 error, etc

    Under the hood, Django just converts HTTP POST and GET objects into a
    'QueryDict', which is a Django dict, which is a Python dict

"""


from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, RequestContext, Http404
from django.utils.decorators import method_decorator # Allow LoggedInMixin
from django.views.generic import TemplateView, View, ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import django_filters

# For debugging
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict
import logging

from .models import Job
from .forms import JobForm
from .serializers import JobSerializer
from rest_framework import viewsets, authentication, permissions, filters


# Debugging: Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger = logging.getLogger(__name__)  # get instance of a logger


class LoggedInMixin(object):
    """ Mixin to ensure user is logged in """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


def find_job(request):
    """ 'Find Job' Page """
    my_data = Job.objects.filter(active=True).order_by('timestamp_created')
    context = {'my_data': my_data}
    return render(request, 'find_job.html', context)


def post_job(request):
    """ 'Post Job' Page """
    if request.method == 'POST':
        form = JobForm(data=request.POST)  # create form, populate data from request
        if form.is_valid():

            #Return authenticated user, if any
            #username = None
            #if request.user.is_authenticated():
            #    username = request.user.username

            company = form.cleaned_data['company']
            location = form.cleaned_data['location']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            salary_min = form.cleaned_data['salary_min']
            salary_max = form.cleaned_data['salary_max']

            my_data = Job(created_by=request.user, company=company,
                         location=location, timestamp_created=timezone.now(),
                         title=title, description=description, status=status,
                         salary_min=salary_min, salary_max=salary_max)

            my_data.save()
            messages.success(request, 'Thanks!')
            return HttpResponseRedirect('/')
    else:  # Request is a 'GET' instead of 'POST'
        form = JobForm()  # get a blank form
        #logger.info("Not a POST")
    return render(request, 'post_job.html', {'form': form})


def manage_job_posts(request):
    """ 'Manage Job Posts' Page """
    my_data = Job.objects.filter(active=True).order_by('timestamp_created')
    context = {'my_data': my_data}
    return render(request, 'manage_job_posts.html', context)


class JobCreateView(LoggedInMixin, CreateView):
    """ Allow Users to Create Jobs """
    model = Job
    template_name = "job_create.html"

    def get_success_url(self):
        """ After posting job, go to job management """
        return reverse('job-post')

    def get_context_data(self, **kwargs):
        context = super(JobCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('job-create')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(LoggedInMixin, UpdateView):
    """ Allow Users to Update Job """
    model = Job
    template_name = 'job_update.html'

    def get_success_url(self):
        """ After updating a job, takes you back to job profile """
        return reverse('manage_job_posts')

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Job.objects.filter(id=specific_id)


class JobListView(LoggedInMixin, ListView):
    """ View a specific job """
    model = Job
    template_name = "job_view.html"

    def get_success_url(self):
        return reverse('job-list')

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Job.objects.filter(id=specific_id)


class JobDeleteView(LoggedInMixin, DeleteView):
    """ Delete a specific job """
    model = Job
    template_name = "job_delete.html"

    def get_success_url(self):
        """ After deleting a job, takes you back to profile """
        return reverse('manage_job_posts')

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Job.objects.filter(id=specific_id)



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

class JobFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(name='company')

    class Meta:
        model = Job
        fields = ('timestamp_updated', 'company', 'title')


# DRF VIEWSETS

class JobViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_class = JobFilter
    search_fields = ('name')
    ordering_fields = ('timestamp_updated')
