#!/usr/bin/env bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn webcrm.wsgi --bind 0.0.0.0:$PORT
python manage.py createsuperuser --noinput
