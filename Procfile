web: gunicorn jobwaffle.wsgi --log-file -
web: newrelic-admin run-program python manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
heroku config:set NEW_RELIC_APP_NAME='JobWaffle'