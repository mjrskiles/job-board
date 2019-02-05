#! bin/bash

python3 -m virtualenv env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8000