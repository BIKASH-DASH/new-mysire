from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models
from django.utils import timezone 

# Create your models here.

class Category(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=250)

    def __str__(self):
      return self.title



class Blog(models.Model):
    """
    Description: Model Description
    """
    title        = models.CharField(max_length=250)
    description  = HTMLField()
    image        = models.FileField(max_length=250)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date     = models.DateTimeField(default=timezone.now())
    meta_title   = models.CharField(max_length=250,blank=True)
    meta_description = HTMLField(blank=True)

    def __str__(self):
      return self.title


