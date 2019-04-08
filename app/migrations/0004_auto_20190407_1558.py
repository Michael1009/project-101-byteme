# Generated by Django 2.1.5 on 2019-04-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='json',
            new_name='endorsements',
        ),
        migrations.AddField(
            model_name='profile',
            name='endorse',
            field=models.IntegerField(default=0),
        ),
    ]
