# Generated by Django 3.2.7 on 2021-09-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servery',
            old_name='open_saturday',
            new_name='open_saturday_breakfast',
        ),
        migrations.RenameField(
            model_name='servery',
            old_name='open_sunday',
            new_name='open_saturday_dinner',
        ),
        migrations.AddField(
            model_name='servery',
            name='open_saturday_lunch',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servery',
            name='open_sunday_breakfast',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servery',
            name='open_sunday_dinner',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servery',
            name='open_sunday_lunch',
            field=models.BooleanField(default=True),
        ),
    ]
