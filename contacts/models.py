from django.db import models
from companies.models import Company

# Create your models here.



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank= True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

