from django.db import models

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
