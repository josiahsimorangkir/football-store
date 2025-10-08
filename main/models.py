from time import timezone
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('baju', 'Baju'),
        ('aksesoris', 'Aksesoris'),
        ('celana', 'Celana'),
    ]
    name = models.CharField(max_length=100, default="Unnamed Product")
    price = models.IntegerField(default=0)
    description = models.TextField(default="No description available")
    thumbnail = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Uncategorized")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()
    
    