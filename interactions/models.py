from django.db import models 
from django.contrib.auth.models import User
from contacts.models import Contact 
# Create your models here.


class Interaction(models.Model):
    interaction_date = models.DateField()
    call_status = models.CharField(max_length=100)  
    contact_type = models.CharField(max_length=100)  
    demo_status = models.CharField(max_length=100)  
    demo_note = models.CharField(max_length=255)  
    call_note = models.CharField(max_length=255)

    follow_up_date = models.DateField(null=True, blank=True)
    interaction_type = models.CharField(max_length=20)
    # customer = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.interaction_date} - {self.call_status}"

