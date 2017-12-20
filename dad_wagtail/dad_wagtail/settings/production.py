from __future__ import absolute_import, unicode_literals

from .base import *

import dj_database_url

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {'default': dj_database_url.config()}

ALLOWED_HOSTS = ['*']

### SUGGESTED BY manage.py check --deploy
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
