# Flask-Alembic #

A [Flask Extension](http://flask.pocoo.org/docs/extensions/) to provide [Alembic](https://bitbucket.org/zzzeek/alembic) integration with [Flask](http://flask.pocoo.org).

## Development Notes ##

* This extension is largely untested at the moment
* in order to provide a correct usage string it currently needs [this fork](https://bitbucket.org/edwardjstone/alembic) of alembic (although it should still work without it)
* there are quite a lot of dependencies and assumptions at the moment
* `init` throws an error when called with arguments

It is intended that these issues will be resolved as development continues! There are probably more bugs than those listed - if you find one please [let us know](https://github.com/tobiasandtobias/flask-alembic/issues).

## Installation ##

Flask-Alembic isn't on pypi yet, so you'll need to install it from the repo:

    $ pip install -e git+https://github.com/tobiasandtobias/flask-alembic.git

This should also install the required dependencies. If you want the usage strings for the management command to be correct, you'll need to do:

    $ pip uninstall alembic

and then

    $ pip install -e hg+https://bitbucket.org/edwardjstone/alembic

to get the forked version.

## Setup ##

First, ensure you have a `SQLAlchemy` object in your flask app:

    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

Please note that one of the assumptions currently made by `Flask-Alembic` is that your `SQLAlchemy` object will be called `db`. If it's not, you can edit the generated alembic `env.py` file appropriately.

The extension provides a [Flask-Script](http://packages.python.org/Flask-Script/) management command wrapper for the `alembic` command, which you will need to add to e.g. `manage.py`:

    from flask.ext.script import Manager
    from flask.ext.alembic import ManageMigrations

    manager = Manager(app)
    manager.add_command("migrate", ManageMigrations())

## Usage ##

You can now use the `alembic` commands using `manage.py migrate`, e.g.

    $ python manage.py migrate -h

There are some differences, however - you can't currently pass any arguments at all to

    $ python manage.py migrate init

or

    $ python manage.py migrate list_templates

since the `ManageMigrations` command hijacks these in order to provide a custom config object, which then supplies the appropriate flask templates to alembic. See the [alembic documentation](http://alembic.readthedocs.org/en/latest/index.html) for more details on the arguments you can use, and how to setup alembic.

## What Flask-Alembic does ##

The extension sub-classes [`alembic.config.Config`](http://alembic.readthedocs.org/en/latest/api.html#alembic.config.Config) in order to provide a set of flask-specific templates (see [`get_template_directory`](http://alembic.readthedocs.org/en/latest/api.html#alembic.config.Config.get_template_directory)). The provided management command then hijacks `init` and `list_templates` in order to pass the flask-specific config.

`manage.py migrate init` uses the flask templates to create an alembic `env.py` that sets the alembic `sqlalchemy.url` config value to the value of `SQLALCHEMY_DATABASE_URI` in the flask config, thereby avoiding repeating the value in more than one place.

It also then imports the `SQLAlchemy` object from the flask app in order to populate `target_metadata` and enable autogeneration of revisions.