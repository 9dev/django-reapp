#!/usr/bin/env python3

from contextlib import contextmanager
from datetime import date
from fabric.api import lcd, local, prefix
import os
import shutil
import sys


###


try:
    APP_NAME = sys.argv[1]
except IndexError:
    print('Usage: python reapp.py MY-APP-NAME')
    exit(0)


###


PREFIX = 'django-'
DJANGO_VERSION = '1.8'
PYTHON_VERSION = '3.4'
PYTHON_PATH = local('which python{}'.format(PYTHON_VERSION), capture=True)
AUTHOR_NAME = local('git config user.name', capture=True)
AUTHOR_EMAIL = local('git config user.email', capture=True)


SAFE_APP_NAME = APP_NAME.replace('-', '_').replace(' ', '_')
FAB_DIR = os.path.dirname(os.path.abspath(__file__))
CWD = os.getcwd()


DEMO_PATH = 'demo'
VENV_PATH = '~/.virtualenvs/' + SAFE_APP_NAME
APP_DIR = CWD + '/' + APP_NAME
DEMO_DIR = '{}/{}'.format(APP_DIR, DEMO_PATH)
FULL_APP_NAME = PREFIX + APP_NAME
SETTINGS_MODULE = 'demo.settings'


###


def init():
    with lcd(FAB_DIR):
        local('rm -f project_template.zip')
        local('zip -r project_template.zip project_template')
        local('rm -f app_template.zip')
        local('zip -r app_template.zip app_template')

    local('virtualenv -p {} {}'.format(PYTHON_PATH, VENV_PATH))
    local('mkdir {}'.format(APP_NAME))


def create_app():
    with lcd(APP_DIR):
        with _venv():
            local('django-admin startproject --template="{}/project_template.zip" --extension=py,txt demo'.format(FAB_DIR))
            local('django-admin startapp --template="{}/app_template.zip" {}'.format(FAB_DIR, SAFE_APP_NAME))


def register_app():
    filename = '{}/demo/settings.py'.format(DEMO_DIR)
    f = open(filename, 'r')
    olddata = f.read()
    f.close()

    newdata = olddata.replace('$APP_SAFE_NAME$', SAFE_APP_NAME)
    f = open(filename, 'w')
    f.write(newdata)
    f.close()


def populate_app():
    create_resource('MANIFEST.in', safe_app_name=SAFE_APP_NAME)
    create_resource('README.md', full_app_name=FULL_APP_NAME, safe_app_name=SAFE_APP_NAME, python_version=PYTHON_VERSION, django_version=DJANGO_VERSION)
    create_resource('LICENSE', year=str(date.today().year), author_name=AUTHOR_NAME)
    create_resource('setup.py', full_app_name=FULL_APP_NAME, safe_app_name=SAFE_APP_NAME, python_version=PYTHON_VERSION, django_version=DJANGO_VERSION, author_name=AUTHOR_NAME, author_email=AUTHOR_EMAIL)
    create_resource('fabfile.py', safe_app_name=SAFE_APP_NAME, venv_path=VENV_PATH, python_path=PYTHON_PATH, demo_path=DEMO_PATH, settings_module=SETTINGS_MODULE)
    create_resource('.gitignore')
    shutil.copytree('{}/resources/fts'.format(FAB_DIR), '{}/fts'.format(APP_DIR))
    register_app()


def install():
    with lcd(APP_DIR):
        local('fab install')
        local('git init')
        local('git add -A')
        local('git commit -m "Initial commit"')


def main():
    init()
    create_app()
    populate_app()
    install()


###


def create_resource(filename, **kwargs):
    with open('{}/resources/{}'.format(FAB_DIR, filename), 'r') as infile:
        with open('{}/{}'.format(APP_DIR, filename), 'w') as outfile:
            for line in infile:
                for src, target in kwargs.iteritems():
                    line = line.replace('{{ ' + src + ' }}', target)
                outfile.write(line)


def _django(command):
    local('python {}/manage.py {}'.format(DEMO_DIR, command))


@contextmanager
def _venv():
    with prefix('. %s/bin/activate' % VENV_PATH):
        yield


###


main()

