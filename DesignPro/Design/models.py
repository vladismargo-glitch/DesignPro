from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    agreement = models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.username})"
