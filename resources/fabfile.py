from contextlib import contextmanager
from fabric.api import cd, local, prefix, shell_env


VENV_PATH = '{{ venv_path }}'
PYTHON_PATH = '{{ python_path }}'

SETTINGS_MODULE = '{{ settings_module }}'
DEMO_PATH = '{{ demo_path }}'


def install():
    local('virtualenv -p {} {}'.format(PYTHON_PATH, VENV_PATH))

    with _venv_local():
        with cd(DEMO_PATH):
            local('pip install -r {}/requirements.txt'.format(DEMO_PATH))

        _django_local('makemigrations')
        _django_local('migrate')


def runserver():
    with _venv_local():
        _django_local('loaddata base.json')
        _django_local('runserver')


def updatedb():
    with _venv_local():
        _django_local('makemigrations')
        _django_local('migrate')


def ftest(target):
    with _venv_local():
        _django_local('test fts.{} -v 2'.format(target))


def utest():
    with _venv_local():
        _django_local('test {{ safe_app_name }}.tests -v 2')


def testall():
    with _venv_local():
        local('rm -f {}/.coverage*'.format(DEMO_PATH))
        local('coverage run -p {}/manage.py test {{ safe_app_name }}.tests -v 2'.format(DEMO_PATH))
        local('coverage run -p {}/manage.py test fts --pattern="*" -v 2'.format(DEMO_PATH))
        local('coverage combine')
        local('coverage report -m --omit="{}/*"'.format(VENV_PATH))
        local('rm -f {}/.coverage*'.format(DEMO_PATH))


def _django_local(command):
    return local(
        'python {}/manage.py {}'.format(DEMO_PATH, command)
    )


@contextmanager
def _venv_local():
    with shell_env(DJANGO_SETTINGS_MODULE=SETTINGS_MODULE):
        with prefix('. %s/bin/activate' % VENV_PATH):
            yield

