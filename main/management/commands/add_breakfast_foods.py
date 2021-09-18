from django.core.management.base import BaseCommand
from ...models import *
import datetime, random
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'adds breakfast meal to every open servery'

    def handle(self, *args, **options):
        for servery in Servery.objects.all():
            if servery.open_now:
                today = datetime.datetime.today()
                meal_end_time = datetime.time(hour=10, minute=30, second=0)
                if today.weekday() >= 5:
                    meal_start_time = datetime.time(hour=8, minute=0, second=0)
                else:
                    meal_start_time = datetime.time(hour=7, minute=30, second=0)
                meal = Meal.objects.get_or_create(
                    servery=servery,
                    meal_type='Breakfast',
                    meal_date=datetime.datetime.today(),
                    meal_start_time=meal_start_time,
                    meal_end_time=meal_end_time,
                )[0]
                dishes = [
                    Dish.objects.get_or_create(
                        name='Scrambled Eggs', eggs=True, vegetarian=True
                    )[0],
                    Dish.objects.get_or_create(
                        name='Biscuits and Gravy', gluten=True, vegetarian=True
                    )[0],
                    Dish.objects.get_or_create(
                        name='Sausage', eggs=True
                    )[0],
                    Dish.objects.get_or_create(
                        name='Vegan Sausage', vegan=True
                    )[0],
                ]
                for dish in dishes:
                    DishAppearance.objects.get_or_create(
                        dish=dish,
                        meal=meal
                    )
