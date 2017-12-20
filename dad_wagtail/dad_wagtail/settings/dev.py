from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l57%nf*_nla8cba(w*(b8w#zi&ligkt%!ve_6-e641x$q%uq_6'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
