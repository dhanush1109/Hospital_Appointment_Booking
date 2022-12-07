from django.db import models

# Create your models here.
class Patients(models.Model):
  name = models.CharField(max_length=255,primary_key=True)
  contactno = models.CharField(max_length=10)
  age = models.CharField(max_length=2)
  reason = models.CharField(max_length=255)