# Generated by Django 5.0.7 on 2024-12-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperAdmin', '0009_student_is_profile_complete_alter_student_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, choices=[('AIDS', 'Artificial Intelligence and Data Science'), ('CSE', 'Computer Science and Engineering'), ('CSIT', 'Computer Science and Information Technology'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering')], default='AIDS', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, default='abc@gmail.com', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='training_type',
            field=models.CharField(blank=True, choices=[('Personal Training', 'Personal Training'), ('Club Member', 'Club Member')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(blank=True, choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year')], null=True),
        ),
    ]
