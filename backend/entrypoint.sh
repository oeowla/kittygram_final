#!/bin/bash

python manage.py migrate --noinput

python manage.py collectstatic --noinput

cp -r /app/collected_static/. /backend_static/

exec "$@"
