from django.db import models
from companies.models import Company
from contacts.models import Contact 
from interactions.models import Interaction


class Dashboard(models.Model):
 
 company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
 contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
 interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE, null=True, blank=True)
 
 def __str__(self):
        return 