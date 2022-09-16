from unicodedata import name
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    overview = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.name