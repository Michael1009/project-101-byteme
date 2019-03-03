# Generated by Django 2.1.5 on 2019-03-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='profile',
            name='courses',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organizations',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]