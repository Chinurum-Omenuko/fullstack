from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)