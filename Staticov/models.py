from django.db import models

class Civilianform(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    ID = models.CharField(db_column='ID', max_length=9)  # Field name made lowercase.
    telephone = models.CharField(max_length=11)
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    religion = models.TextField(db_column='Religion')  # Field name made lowercase.
    age = models.IntegerField()
    place = models.TextField(db_column='Place')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'civilianform'
