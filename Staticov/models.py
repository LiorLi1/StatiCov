from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import django_tables2 as tables 


class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Civilian(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    place = models.TextField(db_column='Place')  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    religion = models.TextField(db_column='Religion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formcivilian'


class Indexform(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    telephone = models.TextField()
    symptoms = models.TextField(db_column='Symptoms')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indexform'


class Registerform(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'registerform'


class Worker(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'worker'

