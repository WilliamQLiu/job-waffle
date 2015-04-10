web: gunicorn jobwaffle.wsgi --log-file -
web: newrelic-admin run-program
heroku config:set NEW_RELIC_APP_NAME='JobWaffle'