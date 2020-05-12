from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    mobile_number=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    userID = models.CharField(max_length=50)


