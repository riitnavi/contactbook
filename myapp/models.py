from django.db import models

# Create your models here.
class contact_table(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)