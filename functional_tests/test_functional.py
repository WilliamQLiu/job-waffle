""" Functional Test == Acceptance Test == End-to-End Test  == Black box Test
    Overview: helps you build an application with the right functionality
    and guarantees that you never accidentally break it.  This kind of test
    looks at how the whole application functions (from the outside) and should
    have human readable code (as in telling a story)

    How to run only functional tests: python manage.py test functional_tests
    How to run unit tests for myapp app only: python manage.py test myapp
    How to run functional and unit tests: python manage.py test

    What this does:
    1.) Starts a Selenium webdriver to pop up a real Firefox browser window
    2.) Use it to open up a web page that we're expecting to be served from the local PC
    3.) Check (making a test assertion) that conditions are met
"""


import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Allows us to enter 'keys'
import time
import pdb


class NewVisitorTest(LiveServerTestCase):
    """ Does landing page load? """

    def spin_assert(self, msg, assertion):
        """ Selenium sometimes works too fast, this retries a few times """
        for i in xrange(60):
            try:
                self.assertTrue(assertion())
                return
            except Exception, e:
                print "Exception", e
                pass
            time.sleep(1)
            self.fail(msg)

    def setUp(self):
        """ setUp runs before each test, like a try in try/except """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # Wait for page to load or else error

    def tearDown(self):
        """ tearDown always runs after each test, even if error """
        self.browser.quit()

    def test_see_main_page_elements_when_not_logged_in(self):
        """ Can see the main page elements like buttons, links """

        # Will needs to enter in some data; he opens up his browser
        self.browser.get('http://localhost:8000')  # Local Dev Env (Hard Coded)
        #self.browser.get('http://www.jobwaffle.com')  # Ubuntu Server
        #self.browser.get(self.live_server_url)  # uses Django's server

        # Notice TITLE
        assert 'Jobwaffle' in self.browser.title, "The Browser Title is " + \
            self.browser.title

        # Notice LOG IN / SIGN UP
        login = self.browser.find_element_by_id('id_log_in')
        self.assertEqual('Log In', login.text)

        signup = self.browser.find_element_by_id('id_sign_up')
        self.assertIn('Sign Up', signup.text)

        # Notice SIDE BAR
        findjob = self.browser.find_element_by_id('id_find_job')
        self.assertIn('Find Job', findjob.text)

        postjob = self.browser.find_element_by_id('id_post_job')
        self.assertIn('Post Job', postjob.text)

        createresume = self.browser.find_element_by_id('id_create_resume')
        self.assertEqual('Create Resume', createresume.text)

        # This only appears if user is authenticated
        #managejobposts = self.browser.find_element_by_id('id_manage_job_posts')
        #self.assertIn('Manage Job Posts', managejobposts.text)


# How a Python script checks if it's been executed from the command
# line rather than being imported by another script
if __name__ == '__main__':

    #unittest.main(warnings='ignore')
    unittest.main()