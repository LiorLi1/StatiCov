from django.db import models

class Civilianform(models.Model):
    id=models.IntegerField(db_column='id',primary_key=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    taz = models.CharField(db_column='TAZ', max_length=9)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    religion = models.TextField(db_column='Religion')  # Field name made lowercase.
    place = models.TextField(db_column='Place')

    class Meta:
        managed = False
        db_table = 'corona_contacts'
