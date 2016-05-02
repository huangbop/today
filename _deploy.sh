#!/bin/bash

export DJANGO_SETTINGS_MODULE='config.settings.production'

export DJANGO_SECRET_KEY='XXX'

export DJANGO_AWS_ACCESS_KEY_ID='XXX'
export DJANGO_AWS_SECRET_ACCESS_KEY='XXX'
export DJANGO_AWS_STORAGE_BUCKET_NAME='XXX'

export DJANGO_MAILGUN_API_KEY='XXX'
export DJANGO_MAILGUN_SERVER_NAME='XXX'

export DATABASE_URL='postgres://postgres:XXX@localhost:/today'

export DJANGO_ALLOWED_HOSTS=mixi.today,XXX
export DJANGO_ADMIN_URL='XXX'


cd /home/projects/today
source ~/.virutalenvs/today/bin/activate
exec ~/.virtualenvs/today/bin/gunicorn -w 3 -b 0.0.0.0:8001 config.wsgi
