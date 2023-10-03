#!/bin/sh

touch /logs/gunicorn.log
touch /logs/gunicorn-access.log
tail -n 0 -f /logs/gunicorn*.log &

# python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn django_project.wsgi:application --bind 0.0.0.0:8000

exec gunicorn django_project.wsgi:application \
    --bind 0.0.0.0:80 \
    --log-level=info \
    --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/gunicorn-access.log
"$@"