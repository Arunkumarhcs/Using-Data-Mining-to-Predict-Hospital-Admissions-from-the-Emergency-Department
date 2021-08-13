from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)

class PatentModel(models.Model):
    patentid=models.IntegerField()
    panentname=models.CharField(max_length=300)
    age=models.IntegerField()
    problem=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    moblenumber=models. BigIntegerField()
    mail=models.EmailField(max_length=400)
    gender=models.CharField(max_length=100)
    ward_type=models.CharField(max_length=100)
    reason=models.CharField(max_length=500)
    date=models.CharField(max_length=100)
    year=models.IntegerField()
    usid=models.ForeignKey(RegisterModel)