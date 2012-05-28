#!/usr/bin/env python
import os
import sys

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
APPS = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(0, APPS)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "billbirder.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
