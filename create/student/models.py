from django.db import models
class test(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    phonenumber=models.BigIntegerField()
    def __str__(self):
       return self.name

# Create your models here.
