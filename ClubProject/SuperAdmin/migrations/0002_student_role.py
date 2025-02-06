# Generated by Django 5.0.7 on 2024-12-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Super Admin', 'Super admin'), ('Club incharge', 'Club incharge'), ('Report Manager', 'Report Manager')], default='Student', max_length=20),
        ),
    ]
