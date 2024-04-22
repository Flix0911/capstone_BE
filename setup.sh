#!/usr/bin/env bash

# exit when the command fails
set -o errexit

# install dependencies
pip install -r memories/requirements.txt

# run migration
python manage.py migrate