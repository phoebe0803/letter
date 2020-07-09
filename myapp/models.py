from django.db import models
class User(models.Model):
    username = models.CharField(max_length=64)
    password= models.CharField(max_length=64)
    email = models.CharField(max_length=64)

class Letter(models.Model):
    username = models.CharField(max_length=64)
    context = models.CharField(max_length=512)
    letter_topic=models.CharField(max_length=64,default='')
    right=models.CharField(max_length=64,default='')
    flag=models.CharField(max_length=64,default='')

