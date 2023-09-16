#!/bin/bash
cd /home/apps/allegro_fucker/


echo "-----------Apply migration--------- "
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations timetracker_api
python manage.py migrate timetracker_api

echo "-----------Create superuser--- "
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi


echo "-----------Run server--------- "
python manage.py runserver 0.0.0.0:8000