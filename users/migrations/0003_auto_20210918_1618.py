# Generated by Django 3.2.7 on 2021-09-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='food_factor',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='walking_factor',
            field=models.IntegerField(default=5),
        ),
    ]
