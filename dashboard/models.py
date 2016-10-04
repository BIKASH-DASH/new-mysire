from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models
from django.utils import timezone 

# Create your models here.



class Page(models.Model):
    title = models.CharField(max_length=250)
    description = HTMLField()
    pub_date     = models.DateTimeField(default=timezone.now())
    meta_title   = models.CharField(max_length=250,blank=True)
    meta_description = HTMLField(blank=True)

    def __str__(self):
      return self.title

class WhatWeDo(models.Model):
    title = models.CharField(max_length=250)
    description  = HTMLField()
    image        = models.FileField(max_length=250)
    pub_date     = models.DateTimeField(default=timezone.now())
    meta_title   = models.CharField(max_length=250,blank=True)
    meta_description = HTMLField(blank=True)

    def __str__(self):
      return self.title

class Social(models.Model):
    """
    Description: Model Description
    """
    link  = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    logoclass = models.CharField(max_length=250)