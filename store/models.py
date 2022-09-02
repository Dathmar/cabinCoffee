from django.db import models


# Create your models here.
class Location(models.Model):
    description = models.CharField(max_length=4000)


class News(models.Model):
    description = models.CharField(max_length=4000)
