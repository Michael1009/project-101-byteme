# Generated by Django 2.1.5 on 2019-04-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190421_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='courses',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organizations',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
