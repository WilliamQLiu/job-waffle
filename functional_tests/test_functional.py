""" Functional Test == Acceptance Test == End-to-End Test  == Black box Test
    Overview: helps you build an application with the right functionality
    and guarantees that you never accidentally break it.  This kind of test
    looks at how the whole application functions (from the outside) and should
    have human readable code (as in telling a story)

    How to run only functional tests: python manage.py test functional_tests
    How to run unit tests for applicant app only: python manage.py test applicant
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



### Setup
class NewVisitorTest(LiveServerTestCase):
    """ Does landing page load? """

    def spin_assert(self, msg, assertion):
        """ Selenium sometimes works too fast, this retries a few times """
        for i in xrange(60):
            try:
                self.assertTrue(assertion())
                return
            except Exception, e:
                pass
            time.sleep(1)
            self.fail(msg)


    def setUp(self):
        """ setUp runs before each test, like a try in try/except """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # Wait for page to load or else error

    def tearDown(self):
        """ tearDown runs after each test, even if there's an error during the test itself """
        self.browser.quit()

    def test_see_main_page_elements(self, text="Jobwaffle", msg=None):
        """ Can see the main page elements like buttons, links """
        # Will needs to enter in some data; he opens up his browser
        self.browser.get('http://localhost:8000')  # Local Dev Env (Hard Coded)

        #time.sleep(5)
        #msg = msg or " waiting for text %s to appear" % text
        #assertion = lambda: self.selenium.is_text_present(text)
        #self.spin_assert(msg, assertion)

        #self.browser.get('http://10.1.1.7')  # Ubuntu Server
        #self.browser.get(self.live_server_url)  # uses Django's server

        # Will notices the page title
        #self.assertIn('Jobwaffle', self.browser.title)
        #assert 'Jobwaffle' in self.browser.title , "The Browser Title is " + self.browser.title

    """

        # Will notices the 'Home' text
        home_nav_bar = self.browser.find_element_by_id('home')
        #print type(sign_in_button)  #<class selenium.webdriver.remote.webelement.WebElement
        #print sign_in_button.text
        self.assertEqual(home_nav_bar.text, 'Home')

        # Will notices the 'Sign In' button
        sign_in_button = self.browser.find_element_by_id('login')
        #print type(sign_in_button)  #<class selenium.webdriver.remote.webelement.WebElement
        #print sign_in_button.text
        self.assertEqual(sign_in_button.text, 'Sign In')

        # Will notices the 'Register' button
        register_button = self.browser.find_element_by_id('register')
        #print type(sign_in_button)  #<class selenium.webdriver.remote.webelement.WebElement
        #print sign_in_button.text
        self.assertEqual(register_button.text, 'Register')

    """

    """
    def test_click_main_page_links(self):
        ''' Can click through to the main page's links '''
        # Click through all the buttons
        home_nav_bar = self.browser.find_element_by_id('home')
        self.browser.click(home_nav_bar)
    """

        # Will enters the registration information and sends an activation email

        # Will confirms the activation email

        # Will clicks on the 'Sign In' tab

        # Will forgets his password 'Forgot'

        # Will has an account and now signs in


# How a Python script checks if it's been executed from the command
# line rather than being imported by another script
if __name__ == '__main__':

    #unittest.main(warnings='ignore')
    unittest.main()