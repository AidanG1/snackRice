# Generated by Django 3.2.7 on 2021-09-18 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, max_length=250, null=True)),
                ('eggs', models.BooleanField(default=False)),
                ('fish', models.BooleanField(default=False)),
                ('gluten', models.BooleanField(default=False)),
                ('milk', models.BooleanField(default=False)),
                ('peanuts', models.BooleanField(default=False)),
                ('shellfish', models.BooleanField(default=False)),
                ('soy', models.BooleanField(default=False)),
                ('tree_nuts', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DishAppearance',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dish')),
            ],
        ),
        migrations.CreateModel(
            name='Servery',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=40)),
                ('image', models.URLField(max_length=250)),
                ('open_friday_dinner', models.BooleanField(default=True)),
                ('open_saturday', models.BooleanField(default=True)),
                ('open_sunday', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Serveries',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('stars', models.IntegerField()),
                ('review_datetime', models.DateTimeField(auto_now_add=True)),
                ('review_text', models.TextField(blank=True, null=True)),
                ('dish_appearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dishappearance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=10)),
                ('meal_date', models.DateField()),
                ('meal_start_time', models.TimeField()),
                ('meal_end_time', models.TimeField()),
                ('servery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servery')),
            ],
        ),
        migrations.AddField(
            model_name='dishappearance',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meal'),
        ),
    ]
