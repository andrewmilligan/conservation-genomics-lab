from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


SECRET_KEY = os.environ['WAGTAIL_SECRET_KEY_CGRI']

# Setup output directory for wagtail-bakery
BUILD_DIR = os.environ['WAGTAIL_DOCUMENT_ROOT_CGRI']

ALLOWED_HOSTS = ['*']

### SUGGESTED BY manage.py check --deploy
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
