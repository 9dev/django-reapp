import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='{{ full_app_name }}',
    version='0.1',
    packages=['{{ safe_app_name }}'],
    include_package_data=True,
    license='MIT License',
    description='...',
    long_description=README,
    url='...',
    author='{{ author_name }}',
    author_email='{{ author_email }}',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: {{ python_version }}',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django >= {{ django_version }}',
    ],
)
