from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=100)

