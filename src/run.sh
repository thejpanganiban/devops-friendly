#/bin/bash

gunicorn -b $HOST:$PORT server:app
