#!/bin/bash
python3 manage.py makemigrations authentication
python3 manage.py makemigrations articles
python3 manage.py migrate
service cron start
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000
