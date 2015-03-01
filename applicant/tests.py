"""
    Unit Tests help you write code that is clean and bug free
    Each line of production code we write should be tested by at least
    one of our unit tests

    Run specific tests for an application using:
    $python manage.py test --settings=jobwaffle.settings.dev_will

    COVERAGE
    Check test coverage with:
        $coverage run manage.py test --settings=jobwaffle.settings.dev_will
    Run test coverage report with: coverage html --include="applicant/*.*" and
    then look under folder 'htmlcov' > 'index.html'
"""


import time  # For debugging

from django.contrib.auth.models import User
from django.conf import settings

from django.core.urlresolvers import resolve
from django.test import TestCase  # Augmented version of std unittest.TestCase
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.db import models
from django.test import TestCase, RequestFactory

from applicant.views import base_page
from employer.views import find_job, post_job


# Blank Page - url(r'^$'')

class SmokeTest(TestCase):
    """ Something simple to check if tests are working """
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class MainPageTest(TestCase):
    #fixtures = ['initial_data']

    def setUp(self):
        """ Every test needs access to the request factory """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='will', email='williamqliu@gmail.com',
            password='enterpassword')
        settings.SITE_ID = 1  # Setup for

    def test_base_url_resolves_to_correct_view(self):
        found = resolve('/')  # resolves this url to map with function in views
        self.assertEqual(found.func, base_page)  # Found the url and function

    def test_base_page_returns_correct_html(self):
        request = HttpRequest()  # What Django sees when browser asks for page
        response = base_page(request)  # pass request to view and get response

        # Get template's html, check that it's the correct response
        expected_html = render_to_string('base.html')
        self.assertEqual(response.content.decode(), expected_html)

        # Decode helps us convert reponse's content bytes to unicode strings
        #print repr(response.content.decode()) # Print response for debugging
        #time.sleep(10)

    def test_find_job_page_resolves_to_correct_view(self):
        found = resolve('/find_job')
        self.assertEqual(found.func, find_job)

    def test_find_job_page_returns_correct_html(self):
        request = HttpRequest()  # What Django sees when browser asks for page
        response = find_job(request)  # pass request to view and get response

        expected_html = render_to_string('find_job.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_post_job_page_resolves_to_correct_view(self):
        found = resolve('/post_job')
        self.assertEqual(found.func, post_job)

    def test_post_job_page_returns_correct_html(self):
        request = HttpRequest()  # What Django sees when browser asks for page
        response = post_job(request)  # pass request to view and get response

        expected_html = render_to_string('post_job.html')
        self.assertEqual(response.content.decode(), expected_html)


if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
