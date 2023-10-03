#!/bin/bash

# Collect static files
echo "Collecting Static Files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying Migrations"
python manage.py makemigrations
python manage.py migrate

# Start Server
echo "Starting Server"
exec "$@"