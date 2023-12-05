from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.IntegerField()