# coding=utf-8
""" Project settings """

from os import environ
from os.path import join, dirname, expanduser
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

VAGRANT_BIN = environ.get('VAGRANT_BIN', default='/usr/bin/vagrant')
VAGRANT_HOME = environ.get('VAGRANT_HOME', default=expanduser('~/vagrant.d'))

VAGRANT_DEFAULT_PROVIDER = environ.get('VAGRANT_DEFAULT_PROVIDER', default='virtualbox')

VAGRANT_MACHINES_STATE_FILE = environ.get(
    'VAGRANT_MACHINES_STATE_FILE',
    default="{0}/{1}".format(VAGRANT_HOME, "data/machine-index/index")
)

DEBUG = environ.get('DEBUG', default=True)

environ['PATH'] = environ.get('SYS_PATH')

