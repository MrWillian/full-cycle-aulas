# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lesson(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
