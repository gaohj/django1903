from django.db import models
# Create your models here.
from django.core import validators

class User(models.Model):
    username = models.CharField(max_length=30,validators=[validators.MinLengthValidator(6)])
    password = models.CharField(max_length=30,validators=[validators.MinLengthValidator(6)])
    telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}')])

