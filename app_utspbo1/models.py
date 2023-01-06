from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Status(models.Model):
    statuspenyu = models.CharField(max_length=100)

    def __str__(self):
        return self.statuspenyu

class Konservasi(models.Model):
    provinsi = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    jenis_penyu = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True)
    Status_keberadaan = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.provinsi