from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
