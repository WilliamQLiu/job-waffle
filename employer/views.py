from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, RequestContext, Http404
from django.utils.decorators import method_decorator # Allow LoggedInMixin
from django.views.generic import TemplateView, View, ListView, UpdateView, DeleteView, CreateView

from .models import Job
from .forms import JobForm

'''def home(request):
    """ Just a blank homepage """
    return render_to_response("base.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )
'''


class JobSearchView(ListView):
    model = Job
    template_name = 'search.html'

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super(JobSearchView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Job.objects.all()


class LoggedInMixin(object):
    """ Mixin to ensure user is logged in """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class JobAllView(LoggedInMixin, ListView):
    """ List all Jobs """
    model = Job
    template_name = "job_all.html"

    def get_success_url(self):
        return reverse('job-all')

    def get_queryset(self):
        return Job.objects.all()

    '''
    def form_valid(self, form):
        job_image = Job(
            image = self.get_form_kwargs().get('files')['image'])
        job_image.save()
        self.id = job_image.id'''


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


class JobPostView(LoggedInMixin, ListView):
    model = Job
    template_name = 'job_posting.html'

    def get_success_url():
        #name = self.request.user.username
        #return reverse('job-post', args=[name])
        return('job-post')

    def get_queryset(self):
        """ Get your job postings """
        return Job.objects.filter(created_by_id=self.request.user)


class JobUpdateView(LoggedInMixin, UpdateView):
    """ Allow Users to Update Job """
    model = Job
    template_name = 'job_update.html'

    def get_success_url(self):
        """ After updating a job, takes you back to job profile """
        #name = self.request.user.username
        #return reverse('job-all', args=[name])
        return reverse('job-post')

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
        return reverse('job-post')

    def get_queryset(self):
        specific_id = self.kwargs['pk']  # Pass variable 'pk' from urls.py
        return Job.objects.filter(id=specific_id)

