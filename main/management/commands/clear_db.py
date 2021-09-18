from django.core.management.base import BaseCommand
from ...models import *


class Command(BaseCommand):
    help = 'clear dishes and meals'

    def handle(self, *args, **options):
        for dish in Dish.objects.all():
            dish.delete()
        for meal in Meal.objects.all():
            meal.delete()
