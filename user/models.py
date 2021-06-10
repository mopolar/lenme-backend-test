from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=150, blank=True)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'