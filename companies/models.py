from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
