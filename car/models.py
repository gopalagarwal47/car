from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    textarea = models.TextField()

def __str__(self):
    return  'message from' + self.name 

class Service(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    company=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
