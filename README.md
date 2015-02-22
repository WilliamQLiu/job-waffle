JobWaffle
======

**Goal**

[Jobwaffle](https://www.jobwaffle.com) will help you find a job you're interested and passionate about.  Using machine learning, we'll match employees and employers.

![Prototype](https://github.com/WilliamQLiu/job-waffle/blob/master/docs/search.png "Prototype")

**Setup**

Jobwaffle is open source.  There's a lot of technical setup so stick with the installation steps below.  The site is currently hosted on a free heroku tier so it'll probably run really slow on live.


**secret.py**

In 'secret.py', enter your own fields for SECRET_KEY, AWS_ACCESS_KEY_ID, EMAIL_HOST, etc.  The version on GitHub are fake info.  Don't push your version of secret.py onto version control (add to your .gitignore file).


**Create the Postgresql database**

Launch the postgresql db before running the django server.


**Setting up Login (Social Auth)**

Jobwaffle allows you to sign up using a social media account (e.g. Facebook, Google Plus, Twitter) thanks to the django-allauth library.  At this moment, you'll need to set up your social account in the database before the site will work.

1. Go to [Facebook's Developer Program](https://developers.facebook.com/apps/) and register your application
2. You'll get a `Client ID` and `Secret key`
3. Under the [Django admin](http://localhost:8000/admin/socialaccount/socialapp/add/), add provider 'Facebook' under 'Social Accounts', 'Social Applications'.
4. Make sure to add in the actual site (e.g. www.jobwaffle.com) as well as available sites (`127.0.0.1:8000` and `localhost:8000`)


**Python Environment**

*  Use 'pip', virtualenv', and 'virtualenvwrapper'
*  Make virtualenv: $`mkvirtualenv jobwaffle`
*  Activate virtualenv: $`workon jobwaffle`
*  Install requirements: $`pip install -r requirements.txt`


**Launch Django Server**

*  Get static files: $`python manage.py collecstatic`
*  Sync the database: $`python manage.py migrate`
*  Launch dev server: $`python manage.py runserver --setting=jobwaffle.settings.dev_will`


**Launch on Heroku**

1. Login: $`heroku login`
2. Create Heroku app: $`heroku create`
3. Rename Heroku app: $`heroku rename jobwaffle`
4. Push code to Heroku `git push heroku master`


**Testing**

* Run only functional tests using: $`python manage.py test functional_tests`
* Run only unit tests using: $`coverage run manage.py test --settings=jobwaffle.settings.dev_will`
* Run both functional and unit tests using: $`python manage.py test --settings=jobwaffle.settings.dev_will`

**Travis-CI**

*  `.travis.yml` file is for continuous integration settings
*  TODO: Add test cases, check on push using continuous integration
