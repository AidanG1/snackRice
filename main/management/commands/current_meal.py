from django.core.management.base import BaseCommand
from ...models import *
import datetime


class Command(BaseCommand):
    help = 'Generates current meal'

    def handle(self, *args, **options):
        for servery in Servery.objects.all():
            if servery.open_now:
                meal_type = current_meal_models().split(' ')[1]
                if meal_type == 'Breakfast':
                    meal_end_time = datetime.time(hour=10, minute=30, second=0)
                    if datetime.date.today().weekday() >= 5:
                        meal_start_time = datetime.time(hour=8, minute=0, second=0)
                    else:
                        meal_start_time = datetime.time(hour=7, minute=30, second=0)
                elif meal_type == 'Lunch':
                    meal_start_time = datetime.time(hour=11, minute=30, second=0)
                    meal_end_time = datetime.time(hour=13, minute=0, second=0)
                else:
                    meal_start_time = datetime.time(hour=17, minute=0, second=0)
                    meal_end_time = datetime.time(hour=19, minute=30, second=0)
                Meal.objects.get_or_create(servery=servery, meal_date=datetime.date.today(),
                                           meal_type=meal_type, meal_start_time=meal_start_time,
                                           meal_end_time=meal_end_time)
