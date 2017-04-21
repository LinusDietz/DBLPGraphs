#!/bin/bash

nohup /usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf &

sh parser/updateXML.sh
nohup sh populate_db &


# Start Gunicorn processes
echo Starting Gunicorn.
#exec gunicorn src.dblpGraphs.config.wsgi:application \
    #--bind 0.0.0.0:8000 \
    #--workers 3

python manage.py runserver
