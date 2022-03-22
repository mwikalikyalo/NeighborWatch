from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

# Create your models here.
class Location(models.Model):
  location = models.CharField(max_length=200)

  def __str__(self):
    return self.location

  def save_location(self):
    self.save()

class Category(models.Model):
  category = models.CharField(max_length=100)

  def __str__(self):
    return self.category