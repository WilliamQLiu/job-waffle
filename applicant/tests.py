""" Unit Tests help you write code that is clean and bug free
    Each line of production code we write should be tested by at least
    one of our unit tests

    Run specific tests for an application using: python manage.py test

    COVERAGE
    Check test coverage with:
        $coverage run manage.py test --settings=jobwaffle.settings.dev_will
    Run test coverage report with: coverage html --include="applicant/*.*" and
    then look under folder 'htmlcov' > 'index.html'
"""


import time  # For debugging

from django.core.urlresolvers import resolve
from django.test import TestCase  # Augmented version of std unittest.TestCase
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.db import models
from django.test import TestCase

from applicant.views import Base


# Blank Page - url(r'^$'')

class SmokeTest(TestCase):
    """ A test that will deliberately fail so we can see error output"""
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class MainPageTest(TestCase):

    '''
    def test_root_url_resolves_to_base_view(self):
        found = resolve('/')  # resolves this url to map with function in views
        self.assertEqual(found.func, Base)  # Found the url and function

    def test_base_page_returns_correct_html(self):
        request = HttpRequest()  # What Django sees when browser asks for page
        response = Base(request)  # Pass it to our view 'Base' and get response

        # Get template's html for Base, check that it's the correct response for base view
        expected_html = render_to_string("base.html")
        self.assertEqual(response.content.decode(), expected_html)
        # Decode helps us convert reponse's content bytes to unicode strings
        #print repr(response.content.decode()) # Print response for debugging
        #time.sleep(10)
    '''


if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
