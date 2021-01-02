from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class worker_register(models.Model):
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userid', max_length=9)  # Field name made lowercase.
    name= models.TextField(db_column='name')
    password = models.CharField(db_column='password',max_length=10)

    class Meta:
        managed = True
        db_table = 'worker-register'

class AdminModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='Name')
    taz=models.CharField(db_column='TAZ',max_length=9)
    password=models.TextField(db_column='Password')
    class Meta:
        managed = False
        db_table = 'admin'

class WorkersModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='Name')
    taz=models.CharField(db_column='TAZ',max_length=9)
    password=models.TextField(db_column='Password')
    Type=models.TextField(db_column='type')
    class Meta:
        managed = False
        db_table = 'workers'

class CivilianModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    taz=models.CharField(db_column='TAZ',max_length=9)
    age=models.IntegerField(db_column='AGE')
    place=models.TextField(db_column='Place')
    date=models.DateField(db_column='DATE')
    religion=models.TextField(db_column='Religion')
    class Meta:
        managed = True
        db_table = 'formcivilian'

class IndexFormModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='Name')
    taz=models.CharField(db_column='TAZ',max_length=9)
    tele=models.TextField(db_column='telephone')
    symp=models.TextField(db_column='Symptoms')
    class Meta:
        managed = False
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

class Patientworker(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    telephone = models.CharField(max_length=11)
    taz = models.CharField(max_length=9)
    workerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patientworker'