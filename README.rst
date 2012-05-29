The ResponderMaps Common Operating Picture Platform, now under
development, is a map sharing system for emergency management, designed
to help teams coordinate and improve situation awareness.

ResponderMaps will provide a wiki-like interface where participating
organizations can share their map information using open standard
formats. ResponderMaps' layers and live feeds will eventually support
all hazards and all phases of the emergency management process.

The first ResponderMaps pilot project is to assemble a common operating
picture for emergency management in the SF Bay Area. We are working with
a variety of agencies and companies to learn requirements and find
relevant data sets.

This repo contains the source code for the ResponderMaps web service,
which is built on software developed by the `GeoCam Project`_. GeoCam
helps disaster responders get information faster by sharing maps,
photos, and other data using their mobile devices.  The GeoCam team is
part of the `NASA Ames Intelligent Robotics Group`_, and the project is
funded by Google. GeoCam software is released open source and
interoperates using open standards.

.. _GeoCam Project: http://geocamshare.org/

.. _NASA Ames Intelligent Robotics Group: http://ti.arc.nasa.gov/tech/asr/intelligent-robotics/

Installation
============

These installation instructions are a work in progress.  If you follow
the directions and run into problems, let us know!

Requirements
~~~~~~~~~~~~

Our primary development platform for these tools is Ubuntu Linux 11.10
(Oneiric Ocelot), running Python 2.7 and Django 1.4.  For the basic
installation we use Django's built-in development web server with a
SQLite 3.7 database.  For the advanced installation we use the Apache
2.2 web server hosting Python using mod_wsgi 3.3.2, with a MySQL 5.1
database.

We have also successfully installed some of these tools on RedHat
Enterprise Linux 6, Mac OS X 10.6 (Snow Leopard), and an Ubuntu virtual
machine running under VMWare on a Windows host.  However, we do not
officially support those platforms.  Our installation instructions below
assume Ubuntu.

Set Up an Install Location
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  export GEOCAM_DIR=$HOME/projects/geocam # or choose your own
  mkdir -p $GEOCAM_DIR

Get the Source
~~~~~~~~~~~~~~

Check out our latest source revision with::

  cd $GEOCAM_DIR
  git clone git://github.com/geocam/geocamResponderMaps.git

For more information on the Git version control system, visit `the Git home page`_.
You can install Git on Ubuntu with::

  sudo apt-get install git-core

.. _the Git home page: http://git-scm.com/

Optionally Install virtualenv (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Especially for a quick test install, we recommend using the virtualenv_
tool to put the relevant Python packages in an isolated sandbox where
they won't conflict with other Python tools on your system.

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

To install virtualenv, create a sandbox named ``packages``, and
"activate" the sandbox::

  sudo apt-get install python-virtualenv
  mkdir $GEOCAM_DIR/virtualenv
  cd $GEOCAM_DIR/virtualenv
  virtualenv --no-site-packages geocamResponderMaps
  source geocamResponderMaps/bin/activate

After your sandbox is activated, package management tools such as
``easy_install`` and ``pip`` will install packages into your sandbox
rather than the standard system-wide Python directory, and the Python
interpreter will know how to import packages installed in your sandbox.

You'll need to source the ``activate`` script every time you log in
to reactivate the sandbox.

Install Non-Python Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

First install Ubuntu packages::

  # tools for Python package compilation and management
  sudo apt-get install python2.7-dev python-pip

  # basic database
  sudo apt-get install sqlite3 libsqlite3-dev
  
Set Up the Site
~~~~~~~~~~~~~~~

To install Python dependencies, generate initial configuration files,
and collect static files for the server, run::

  cd $GEOCAM_DIR/geocamResponderMaps
  ./manage.py bootstrap --yes
  source $GEOCAM_DIR/geocamResponderMaps/sourceme.sh
  ./manage.py prep

You'll need to source the ``sourceme.sh`` file every time you open a new
shell if you want to run related Python scripts such as starting
the Django development web server.  The ``sourceme.sh`` file will also
take care of activating your virtualenv environment in new shells, if
you were in a virtualenv when you ran ``setup.py``.

To initialize the database::

  $GEOCAM_DIR/geocamResponderMaps/manage.py syncdb

The syncdb script will ask you if you want to create a Django superuser.
We recommend answering 'yes' and setting the admin username to ``root``
for compatibility with our utility scripts.

Try It Out
~~~~~~~~~~

To run the Django development web server::

  $GEOCAM_DIR/geocamResponderMaps/manage.py runserver

Now you're ready to try it out!  If you can open a web browser on the
same host where the server is installed, you can start using the app by
visiting http://localhost:8000/ in that browser.

.. o  __BEGIN_LICENSE__
.. o  Copyright (C) 2008-2010 United States Government as represented by
.. o  the Administrator of the National Aeronautics and Space Administration.
.. o  All Rights Reserved.
.. o  __END_LICENSE__
