from django.db import models

# Create your models here.
class workerlogin(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    days = models.DateField(db_column='days')  # Field name made lowercase.
    numbers=models.IntegerField(db_column='numbers') # Field name made lowercase..
    positive = models.BooleanField(db_column='positive')

    class Meta:
        managed = False
        db_table = 'testgrapgh'


