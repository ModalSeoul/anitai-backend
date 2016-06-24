#! /bin/bash
python /anitai/manage.py migrate --noinput
python /anitai/manage.py runserver 0.0.0.0:8000
