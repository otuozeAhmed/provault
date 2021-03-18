from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GROUP_CHOICES = (
        ('Group_1', 'Group 1'),
        ('Group_2', 'Group 2'),
        ('Group_3', 'Group 3'),
    )
    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
