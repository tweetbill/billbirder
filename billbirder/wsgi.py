import os
import sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
APPS = os.path.join(ROOT, 'apps')
sys.path.insert(0, APPS)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "billbirder.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

