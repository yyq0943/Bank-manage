from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    type = models.CharField(max_length=10)



class List(models.Model):
    lid = models.IntegerField(primary_key=True)
    danger = models.CharField(max_length=255)
    thing = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    money = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    people = models.ForeignKey(User)
    num = models.CharField(max_length=255)


