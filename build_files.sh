#!/bin/bash

# Update package lists and install dependencies
sudo apt update
sudo apt install -y libpq-dev python3-dev

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Ensure the output directory exists
mkdir -p staticfiles_build
mv static staticfiles_build/