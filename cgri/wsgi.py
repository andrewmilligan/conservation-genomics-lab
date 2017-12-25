"""
WSGI config for cgri project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

django_settings_module = "cgri.settings.production"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

# Add the app's directory to the PYTHONPATH
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
if BASE_DIR not in sys.path:
  sys.path.append(BASE_DIR)
if PROJECT_DIR not in sys.path:
  sys.path.append(PROJECT_DIR)

from django.conf import settings

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(os.path.join(settings.VIRTUAL_ENV_DIR, 'lib', 'python2.7',
  'site-packages'))

activate_env = os.path.join(settings.VIRTUAL_ENV_DIR, 'bin', 'activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()
