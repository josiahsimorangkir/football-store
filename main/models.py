from django.db import models

import uuid
from django.db import models

class Product(models.Model):
    
    name = models.CharField
    price = models.IntegerField
    description = models.TextField
    thumbnail = models.URLField
    category = models.CharField
    is_featured = models.BooleanField
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
# Create your models here.
