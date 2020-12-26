from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class AdminModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='password')
    class Meta:
        managed = False
        db_table = 'admin'

class WorkerModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='password')
    class Meta:
        managed = False
        db_table = 'worker'

class CivilianModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    taz=models.CharField(db_column='taz',max_length=9)
    age=models.IntegerField(db_column='age')
    place=models.TextField(db_column='place')
    date=models.DateField(db_column='date')
    religion=models.TextField(db_column='religion')
    class Meta:
        managed = False
        db_table = 'civilianform'

class IndexFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    telephone=models.TextField(db_column='telephone')
    symptomes=models.TextField(db_column='Symptomes')
    class Meta:
        managed = True
        db_table = 'indexform'
   

class RegisterFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    taz=models.CharField(db_column='taz',max_length=9)
    password=models.TextField(db_column='password')
    Type=models.TextField(db_column='type')
    class Meta:
        managed = False
        db_table = 'registerform'