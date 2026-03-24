import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Default admin credentials (used if env vars are not set)
DEFAULT_USERNAME = "Zee01470"
DEFAULT_EMAIL = "admin@globaldash.com"
DEFAULT_PASSWORD = "Zee01470"


class Command(BaseCommand):
    help = "Creates or updates the admin superuser on every deploy."

    def handle(self, *args, **options):
        User = get_user_model()

        # Use env vars if set, otherwise fall back to defaults
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME") or DEFAULT_USERNAME
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL") or DEFAULT_EMAIL
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD") or DEFAULT_PASSWORD

        try:
            user = User.objects.get(username=username)
            user.email = email
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" updated successfully.'))
        except User.DoesNotExist:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
