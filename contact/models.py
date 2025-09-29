from django.db import models

class contacts(models.Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=900)


# Create your models here.
