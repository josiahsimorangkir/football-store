from time import timezone
from django.db import models


class Product(models.Model):
    
    name = models.CharField(max_length=100, default="Unnamed Product")
    price = models.IntegerField(default=0)
    description = models.TextField(default="No description available")
    thumbnail = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, default="Uncategorized")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    
    