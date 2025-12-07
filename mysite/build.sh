#!/usr/bin/env bash
set -o errexit

# Install requirements from the correct folder
pip install -r requirements.txt

# Run Django setup commands
python manage.py collectstatic --noinput
python manage.py migrate
