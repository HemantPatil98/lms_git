#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from .django_adminlte3 import sheetsapi
# from lms import sheetsapi

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_adminlte3.settings')
    try:
        # print("hi")
        from django.core.management import execute_from_command_line
        # sheetsapi.startsheet()

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
