# Generated by Django 2.2 on 2019-04-22 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_skill_pk_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='endorse',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='endorsements',
        ),
    ]
