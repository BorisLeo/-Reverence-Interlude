from django.db import models

# Create your models here.
class Size(models.Model):
    name=models.CharField(max_length=10, unique=True)
    
        
    
        def __str__(self):
            return self.name
    
    class Category(models.Model):
        name=models.CharField(max_length=255, unique=True)