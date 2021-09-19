# Generated by Django 3.2.7 on 2021-09-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210918_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='eggs',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='fish',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='gluten',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='milk',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='peanuts',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='shellfish',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='soy',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='tree_nuts',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='vegan',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='vegetarian',
            field=models.CharField(choices=[('prefer_tag', 'Prefer Tag'), ('no_preference', 'No Preference'), ('prefer_no_tag', 'Prefer No Tag')], default='no_preference', max_length=15),
        ),
    ]
