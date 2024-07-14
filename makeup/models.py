from django.db import models
from django.urls import reverse

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)

    def _str_(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', args=[str(self.id)])

class Product(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.TextField()
    expire_date = models.DateField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])