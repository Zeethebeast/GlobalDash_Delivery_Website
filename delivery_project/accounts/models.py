from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any extra profile fields here later if needed
    is_admin_staff = models.BooleanField(default=False, help_text="Designates whether this user has dashboard management access.")

    def __str__(self):
        return self.username
