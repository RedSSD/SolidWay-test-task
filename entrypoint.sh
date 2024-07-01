#!/bin/bash
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
service cron start
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000