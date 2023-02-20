from django.db import models

# Create your models here.
from django.utils import timezone
from symtable import Class
from django.contrib.auth.models import User


Class Section(models.Model):

    title = models.CharField(max_length=250)
