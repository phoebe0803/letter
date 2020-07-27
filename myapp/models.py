from django.db import models
class User(models.Model):
    username = models.CharField(max_length=64)
    password= models.CharField(max_length=64)
    email = models.CharField(max_length=64)

class Letter(models.Model):
    username = models.CharField(max_length=64)
    context = models.CharField(max_length=512)
    letter_topic=models.CharField(max_length=64,default='')
    # 0,1right(公开 0， 仅自己可见 1)
    right=models.IntegerField()
    #flag:"0,1"(保存草稿 0 ， 投递 1)
    flag=models.IntegerField()
    #delete:"0,1"(1删除了)
    delete=models.IntegerField(default=0)
class Xinli(models.Model):
    topic=models.CharField(max_length=64,default='')
    title= models.CharField(max_length=64)
    context = models.CharField(max_length=512)
    url= models.CharField(max_length=128,default='')
    editor = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    #delete:"0,1"(1删除了)
    delete=models.IntegerField(default=0)
class collect_letter(models.Model):
    username = models.CharField(max_length=64,default='')
    letter_id=models.IntegerField(default=0)


