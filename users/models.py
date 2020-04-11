from django.db import models
from datetime import datetime

class users(models.Model):
    memberId = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    def __str__(self): #Show userName as the identifying field
        return self.userName 
