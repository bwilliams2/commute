#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf import settings


# Add apps subdirectory
print(settings.BASE_DIR)
sys.path.insert(0, str(settings.BASE_DIR.joinpath("backend/apps")))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
