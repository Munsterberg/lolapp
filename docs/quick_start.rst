Quick Start Guide
================

Download the Boilerplate
------------------------

You can download this on GitHub.

Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.

You can generate a secret key here DJANGO_KEY |django_key|
.. |django_key| raw:: html
    
    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>

Project Name
------------

This project is named *Emilia*, so if you're using this boilerplate to create
your own project, you'll have to change the name in a few places:

- *emilia* **folder** -- The top of the project directory.
- *emilia/emilia* **folder** -- Your project name.
- virtual environment names: **emilia** and **emilia_test**.
- in virtual environments **postactivate** where settings are in both
  development and testing.

Virtual environments and Settings Files
---------------------------------------

First, you need to know your python 3 path:
    $ which python3

which is something similar to /usr/local/bin/python3

Next, create a development virtual environment with python 3 installed:
    $ mkvirtualenv --python=/usr/local/bin/python3 emilia

or this may work:
    $ mkvirtualenv -ppython3.5 emilia

Go to the virtual environment folder:
    $ cd $VIRTUAL_ENV/bin

and edit the postactivate file:
    $ vim postactivate

You must add the lines:
    export DJANGO_SETTINGS_MODULE="emilia.settings.development"
    export SECRET_KEY="your_secret_django_key"

with your project name and your own secret key.

Next, edit the **predeactivate** file and add the lines:
    unset DJANGO_SETTINGS_MODULE
    unset SECRET_KEY

**Repeat** this process for a testing environment.

Now you can install the packages in each environment:
    $ workon emilia
    $ pip install -r requirements/development.txt
    $ workon emilia_test
    $ pip install -r requirements/testing.txt
