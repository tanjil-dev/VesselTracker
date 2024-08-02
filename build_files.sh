#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Ensure the output directory exists
mkdir -p staticfiles_build
mv static staticfiles_build/