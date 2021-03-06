# Shop Display

## Description

This project is a simple internal website for displaying useful information on a large TV on the shop floor.

## How to run this project
---

To start the test server and make it available to other machines on the network, run

`python3 manage.py runserver 0.0.0.0:8000`

Open a browser and go to `localhost:8000` to view the app.

Go to `localhost:8000/admin` to enter/manage jobs.

## How to build this project
---
---

### Setting up the development environment
---

The website is built with Django 2 and Python 3. The current plan is to deploy it on an Apache web server running on a raspberry pi 3.

#### Virtual Environment
---

The project is set up to use a virtual python environment to manage package dependencies. Since the shop display is probably the only project that will run on the Pi, this is probably an optional step, but it may help when working on the project on other computers.

On the pi the virtual environment is located at

`<project directory>/env`

The environment can be activated by running from the project directory the shell command

`source ./env/bin/activate`

The environment can be deactivated at any time with

`deactivate`

Any python packages installed using pip while the environment is active will only be installed in the virtual environment. This is useful because any packages that are installed systemwide will not affect the project environment, and also because it provides a record of all project dependencies.

#### requirements.txt
---

Any python packages added with pip should be listed in the requirements.txt file. To automatically update the file: make sure the virtual environment is active, navigate to the project directory (the folder that contains requirements.txt) then run

`pip3 freeze > requirements.txt`

This should be done any time a new package is added with pip.

To install all of the packages listed in the requirements.txt file: make sure the virtual environment is active, navigate to the project directory, then run

`pip3 install -r requirements.txt`

#### Example setup on a new computer
---

Make sure python3 and pip3 are installed. (Installing python3 also installs pip3.)

If you are going to use a virtual environment, you also need the package virtualenv. To install:

`pip3 install virtualenv`

From the command line:

- Navigate to the folder that you would like to place your project folder in
    - `git clone https://github.com/mjrskiles/job-board.git`
    - `cd job-board`
    - `pip3 install -r requirements.txt`
    - `python3 -m virtualenv env`
    - `source env/bin/activate`
    - `python3 manage.py migrate`
    - Then you can run using the instructions at the top

At this point, the project should be ready to run. For help with django, see the django documentation.

## Useful resources

[Deploying a django project with apache on a raspberry pi](https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/)

[Django 2.0 documentation](https://docs.djangoproject.com/en/2.0/)

[Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

--

Need to write a script to install and create a virtual env.
Goal is to be able to execute one script to prepare the environment and one to start the project

---
admin
csi001csi001

## From project directory

python3 -m virtualenv env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8000