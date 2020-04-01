from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Person(model.Models):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.pass
"""

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
