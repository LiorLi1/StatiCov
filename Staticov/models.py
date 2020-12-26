from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Civilianform(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    ID = models.CharField(db_column='ID', max_length=9)  # Field name made lowercase.
    telephone = models.CharField(db_column='telephone',max_length=11)
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    religion = models.TextField(db_column='Religion')  # Field name made lowercase.
    age = models.IntegerField(db_column='age')
    place = models.TextField(db_column='Place')
    email=models.TextField(db_column='email') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'civilianform'

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

class WorkerModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='Name')
    taz=models.CharField(db_column='TAZ',max_length=9)
    password=models.TextField(db_column='Password')
    class Meta:
        managed = False
        db_table = 'worker'

class CivilianModel(models.Model):
    ID=models.IntegerField(db_column='ID',primary_key=True)
    taz=models.CharField(db_column='TAZ',max_length=9)
    age=models.IntegerField(db_column='AGE')
    place=models.TextField(db_column='Place')
    date=models.DateField(db_column='DATE')
    religion=models.TextField(db_column='Religion')
    class Meta:
        managed = False
        db_table = 'civilianform'

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