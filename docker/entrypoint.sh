#!/bin/bash
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py loaddata fixtures/superadmin.json
python manage.py runserver 0.0.0.0:8000
