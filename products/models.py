from __future__ import unicode_literals
from djongo import models
#from django.db.models.signals import m2m_changed

# Create your models here.
class Product(models.Model):
  brand = models.CharField(max_length=50)
  description = models.TextField()
  image = models.CharField(max_length=255)
  price = models.IntegerField(default=0)
  price_offer = None

  def __str__(self):
    return self.description