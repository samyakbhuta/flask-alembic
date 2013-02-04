"""
----------------
  Flask-Alembic
----------------

`Alembic`__ integration for Flask.

__ https://bitbucket.org/zzzeek/alembic/

"""
from setuptools import setup


setup(
    name='Flask-Alembic',
    version='0.1',
    url='',
    license='BSD',
    author='Edward Stone',
    author_email='edwardjstone@yahoo.com',
    description='Alembic integration in Flask.',
    long_description=__doc__,
    packages=['flask_alembic'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'alembic',
        'Flask-SQLAlchemy',
        'Flask-Script',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
