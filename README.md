JobWaffle  [![Build Status](https://travis-ci.org/WilliamQLiu/job-waffle.svg?branch=master)](https://travis-ci.org/WilliamQLiu/job-waffle)  [![Coverage Status](https://coveralls.io/repos/WilliamQLiu/job-waffle/badge.svg?branch=master)](https://coveralls.io/r/WilliamQLiu/job-waffle?branch=master)
======

![Prototype](https://github.com/WilliamQLiu/job-waffle/blob/master/docs/search.png "Prototype")


**Goal**

Jobwaffle will help you find a job you're interested and passionate about.  Using machine learning, we'll match employees and employers.

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

*  Get static files: $`python manage.py collectstatic --setting=jobwaffle.mysettings.dev_will`
*  Sync the database: $`python manage.py migrate --setting=jobwaffle.mysettings.dev_will`
*  Launch dev server: $`python manage.py runserver --setting=jobwaffle.mysettings.dev_will`


**Launch ElasticSearch**

*  On local Mac, start ElasticSearch with: `elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml`
*  To build your search index, do: `python manage.py rebuild_index --settings=jobwaffle.mysettings.dev_will`
*  To rebuild your search index, do: `python manage.py update_index --settings=jobwaffle.mysettings.dev_will`


**Launch on Heroku**

Note: You need to add a 'settings.py' file for Heroku; I'm taking the site off Heroku (even though the below instructions should work).  Instead, I'm using Docker with AWS.  See below on how to setup with Docker.

~~1. Login: $`heroku login`
2. Create Heroku app: $`heroku create`
3. Rename Heroku app: $`heroku rename jobwaffle`
4. Push code to Heroku `git push heroku master`~~


**Docker**

Dockerfile is available on DockerHub [here](https://registry.hub.docker.com/u/williamqliu/job-waffle/dockerfile/)

1.) Install Docker and Docker-Compose on your development machine
2.) Use Docker-Compse to build the dev environment:  `docker-compose run web`
3.) Then run `docker-compose up -d` to run your containers in daemonized mode
4.) Then run `docker-compose run web python manage.py syncdb`
Other helpful options include:
*  `docker run -t jobwaffle_web` to go into container
*  `docker-compose stop` to stop your containers

**Testing**

* Run only functional tests using: $`python manage.py test functional_tests --setting=jobwaffle.mysettings.dev_will`
* Run only unit tests using: $`coverage run manage.py test --settings=jobwaffle.mysettings.dev_will`
* Run both functional and unit tests using: $`python manage.py test --settings=jobwaffle.mysettings.dev_will`
* Get a coverage report using: $`coverage report`
* You can specify to see all the tests with `-v 2` (verbose output) and `-v 3` (very verbose output)


**Travis-CI**

*  `.travis.yml` file is for continuous integration settings.  The idea is that each build is checked in and verified by an automated build to detect problems early.  
*  Builds shown [here](https://travis-ci.org/WilliamQLiu/job-waffle)


**Coveralls**

*  Coveralls shows how much of your project is covered by tests.  
*  Coverage shown [here](https://coveralls.io/r/WilliamQLiu/job-waffle)


