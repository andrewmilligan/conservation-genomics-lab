from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


SECRET_KEY = os.environ['CGRI_SECRET_KEY']

# Setup output directory for wagtail-bakery
BUILD_DIR = os.environ['CGRI_DOCUMENT_ROOT']

ALLOWED_HOSTS = ['*']

### SUGGESTED BY manage.py check --deploy
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
