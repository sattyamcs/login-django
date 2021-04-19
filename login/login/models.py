from django.db import models

class Newuser(models.Model):
    Email = models.CharField(max_length=150)
    Pwd = models.CharField(max_length=150)
    Firstname = models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)
    Phone = models.CharField(max_length=12)
    Address = models.CharField(max_length=150)
    Gender = models.CharField(max_length=1)
