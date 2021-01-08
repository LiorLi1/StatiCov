# Generated by Django 3.1.5 on 2021-01-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name')),
                ('taz', models.CharField(db_column='taz', max_length=9)),
                ('password', models.TextField(db_column='Password')),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CivilianModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('taz', models.CharField(db_column='taz', max_length=9)),
                ('age', models.IntegerField(db_column='age')),
                ('place', models.TextField(db_column='place')),
                ('date', models.DateField(db_column='date')),
                ('religion', models.TextField(db_column='religion')),
            ],
            options={
                'db_table': 'formcivilian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='emploiedutemp',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('startdate', models.TextField(db_column='startdate')),
                ('enddate', models.TextField(db_column='enddate')),
                ('workerid', models.CharField(db_column='workerid', max_length=9)),
                ('confirmation', models.TextField(db_column='confirmation')),
            ],
            options={
                'db_table': 'emploiedutemp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexFormModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name')),
                ('taz', models.CharField(db_column='taz', max_length=9)),
                ('telephone', models.CharField(db_column='telephone', max_length=11)),
                ('symptomes', models.TextField(db_column='symptomes')),
                ('age', models.CharField(db_column='age', max_length=3)),
                ('workerid', models.IntegerField(db_column='workerid')),
            ],
            options={
                'db_table': 'indexform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SymptomesFormModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('head', models.TextField(db_column='head')),
                ('hot', models.TextField(db_column='hot')),
                ('smell', models.TextField(db_column='smell')),
                ('hurts', models.TextField(db_column='hurts')),
            ],
            options={
                'db_table': 'symptomesform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patientworker',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('telephone', models.CharField(max_length=11)),
                ('taz', models.CharField(max_length=9)),
                ('workerid', models.IntegerField(db_column='workerid')),
            ],
            options={
                'db_table': 'patientworker',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('mid', models.IntegerField(db_column='MID', primary_key=True, serialize=False)),
                ('popupmsg', models.TextField(db_column='popupmsg')),
            ],
            options={
                'db_table': 'popup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RegisterFormModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name')),
                ('taz', models.CharField(db_column='taz', max_length=9)),
                ('password', models.TextField(db_column='password')),
                ('Type', models.TextField(db_column='type')),
                ('civiliantype', models.TextField(db_column='civiliantype')),
            ],
            options={
                'db_table': 'registerform',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='worker_register',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.CharField(db_column='userid', max_length=9)),
                ('name', models.TextField(db_column='name')),
                ('password', models.CharField(db_column='password', max_length=10)),
            ],
            options={
                'db_table': 'worker-register',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkersModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name')),
                ('taz', models.CharField(db_column='taz', max_length=9)),
                ('password', models.TextField(db_column='password')),
                ('Type', models.TextField(db_column='type')),
            ],
            options={
                'db_table': 'workers',
                'managed': True,
            },
        ),
    ]
