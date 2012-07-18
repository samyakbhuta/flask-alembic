import argparse
from alembic.config import main as console_script
from alembic.config import Config
from alembic.command import init, list_templates
from flask.ext.script import Command
import os

__all__ = ('FlaskAlembicConfig', 'ManageMigrations', )

class FlaskAlembicConfig(Config):

    def __init__(self, file_=None):
        super(FlaskConfig, self).__init__(file_)

    def get_template_directory(self):
        package_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(package_dir, 'templates')

class CatchAllParser(object):
    def parse_known_args(self, app_args):
        return argparse.Namespace(), app_args

class ManageMigrations(Command):
    """Manage alembic migrations"""
    capture_all_args = True

    def __init__(self, impl=console_script):
        self.implementation = impl

    def create_parser(self, prog):
        return CatchAllParser()

    def run(self, args):

        # let's hijack init and list_templates
        # we want to provide our own config object
        # in order to provide a custom get_template_directory function
        if args[0] in ['list_templates', 'init']:
            config = FlaskAlembicConfig("alembic.ini")
            if args[0] is 'list_templates':
                return list_templates(config)
            else:
                return init(config, 'flask-alembic', template='flask')

        import sys, os.path
        prog = '%s %s' % (os.path.basename(sys.argv[0]), sys.argv[1])

        return self.implementation(args, prog)