# django-reapp

Framework for developing reusable Django apps. Instead of preparing it from a scratch, you can focus on building the essence of your app.

## Features

`django-reapp` provides:

* application base structure
* demo project
* virtualenv for demo
* admin:admin account in demo
* automated package provisioning
* git repository
* fabfile

## Structure

For app named `my-test`, `django-reapp` generates the following:

    my-test
    ├── demo
    │   ├── db.sqlite3
    │   ├── demo
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── fixtures
    │   │   │   └── base.json
    │   │   ├── __init__.py
    │   │   ├── migrations
    │   │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── static
    │   │   │   └── main
    │   │   │       └── base.css
    │   │   ├── templates
    │   │   │   ├── base.html
    │   │   │   └── main
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── manage.py
    │   └── requirements.txt
    ├── fabfile.py
    ├── fts
    │   ├── _base.py
    │   ├── Dummy.py
    │   └── __init__.py
    ├── LICENSE
    ├── MANIFEST.in
    ├── my_test
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── README.md
    └── setup.py

## Usage

To create a new app named `myapp` in the current directory, type:

    > python2.7 path/to/reapp.py myapp

Make sure to review the generated documents. You probably want to change things like app description.

### Demo

To start a demo project at ``127.0.0.1:8000``, execute `fab runserver`.

## Customization

If you want to adjust things like Django version or application prefix, edit `reapp.py` file directly.
