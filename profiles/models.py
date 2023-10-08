from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    typing_speed = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)

    # Specify related_name to avoid clashes
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profiles_user_permissions',
        blank=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profiles_user_groups',
        blank=True,
    )


    def __str__(self):
        return self.username

class Exercise(models.Model):
    text = models.TextField()
    difficulty_level = models.CharField(max_length=20)

    def __str__(self):
        return f"Exercise {self.id}"
