#!/bin/sh

until cd /app/
do
    echo "Waiting for server volume..."
done

until python manage.py makemigrations --noinput
do
     echo "Waiting for db to be ready..."
     sleep 2
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8000
