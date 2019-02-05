#! bin/bash

sudo pip3 install virtualenv
source env/bin/activate
python3 -m virtualenv env
pip3 install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8000
