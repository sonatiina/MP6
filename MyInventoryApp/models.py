from django.db import models
from django.utils import timezone

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    def getName(self):
        return self.name
    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"
class WaterBottle(models.Model):
    sku = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=19, decimal_places=10)
    size = models.CharField(max_length=300)
    mouth_size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.BigIntegerField()
    def __str__(self):
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplier}, {self.cost}: {self.current_quantity}"