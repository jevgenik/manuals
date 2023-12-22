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


.. tip::
   A **model** is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 
   Django follows the DRY (Don’t repeat yourself) Principle. The goal is to define your data model in one place and automatically derive things from it.
  
   This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely derived from your models file, and are essentially a  
   history that Django can roll through to update your database schema to match your current models.

Django installation
===================

#. Install Python 3.6 or higher (e.g ``sudo apt-get install python3.6`` or on Windows `download <https://www.python.org/downloads/windows/>`_ and install)
#. Install Django (e.g. ``pip install django``)

Django commands
===============

* ``django-admin startproject <project_name>`` - create a new project
  
* ``python manage.py runserver`` - run the web server (default port is 8000) to acceess it go to ``http://localhost:8000``

* ``py manage.py startapp <app_name>`` - create a new app (app is a part of a project)

* ``py manage.py migrate`` - look at the INSTALLED_APPS setting and create any necessary database tables according to the database settings in your mysite/settings.py  
  file and the database migrations shipped with the app

* ``py manage.py makemigrations`` - create migrations for changes in the models (in other words, it creates a file which contains SQL commands to create tables in the database)