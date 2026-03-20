from django.db import models


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER
    )

    def __str__(self):
        return self.fullName 