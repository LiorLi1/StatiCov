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


class index_form(models.Model):
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='name')  # Field name made lowercase.
    taz = models.CharField(db_column='taz',max_length=9) # Field name made lowercase..
    telephone = models.CharField(db_column='telephone',max_length=11)
    symptomes = models.TextField(db_column='symptomes')
    class Meta:
        managed = False
        db_table = 'indexform'

class worker_register(models.Model):
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userid', max_length=9)  # Field name made lowercase.
    name= models.TextField(db_column='name')
    password = models.CharField(db_column='password',max_length=10)

    class Meta:
        managed = True
        db_table = 'worker-register'

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created, **kwargs):
        if created:
           worker_register.objects.create(user=instance)
        instance.profile.save() 