#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
    try:
        from django.core.management import execute_from_command_line
        # add these lines for loading data
        if len(sys.argv) == 2 and sys.argv[1] == 'migrate':
            execute_from_command_line(['manage.py', 'loaddata', 'fixtures.json'])
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)