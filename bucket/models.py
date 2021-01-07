from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    prefix = models.CharField(max_length=1000, null=False, blank=False)


class NameException(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)