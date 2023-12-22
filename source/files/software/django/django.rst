======
Django
======
Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.

.. tip::
   Django is named after Django Reinhardt, a jazz manouche guitarist from the 1930s to early 1950s.


`Official website <https://www.djangoproject.com/>`_

`Writing your first Django app <https://docs.djangoproject.com/en/5.0/intro/tutorial01/>`_


.. figure:: images/django_file_structure.png
   :alt: Django File Structure
   
   Django File Structure. `Source <https://www.tutorialspoint.com/django/django_file_structure.htm>`_


Django installation
===================

#. Install Python 3.6 or higher (e.g ``sudo apt-get install python3.6`` or on Windows `download <https://www.python.org/downloads/windows/>`_ and install)
#. Install Django (e.g. ``pip install django``)

Django commands
===============

* ``django-admin startproject <project_name>`` - create a new project
  
* ``python manage.py runserver`` - run the web server (default port is 8000) to acceess it go to ``http://localhost:8000``

* ``py manage.py startapp <app_name>`` - create a new app (app is a part of a project)

* ``py manage.py makemigrations`` - create migrations for changes in the models (in other words, it creates a file which contains SQL commands to create tables in the database)