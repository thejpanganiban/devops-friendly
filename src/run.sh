#/bin/bash

gunicorn -b $HOST:$PORT server:app --access-logfile - --error-logfile -
