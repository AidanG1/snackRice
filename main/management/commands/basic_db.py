from django.core.management.base import BaseCommand
from ...models import *
import datetime, random
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'add a basic database'

    def handle(self, *args, **options):
        serveries = [
            {'slug': 'west', 'name': 'West Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2019-12/west-servery_0.jpg.jpeg?itok=JC0x_3bt',
             'open_friday_dinner': True, 'open_saturday_breakfast': False, 'open_saturday_lunch': False,
             'open_saturday_dinner': False, 'open_sunday_breakfast': True, 'open_sunday_lunch': True,
             'open_sunday_dinner': True},
            {'slug': 'siebel', 'name': 'Siebel Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2019-12/seibel-servery.jpg.jpeg?itok=6v_-ngCG',
             'open_friday_dinner': True, 'open_saturday_breakfast': True, 'open_saturday_lunch': True,
             'open_saturday_dinner': True, 'open_sunday_breakfast': True, 'open_sunday_lunch': True,
             'open_sunday_dinner': True},
            {'slug': 'baker', 'name': 'Baker Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2019-12/baker-servery.jpg.jpeg?itok=afyfCZPr',
             'open_friday_dinner': False, 'open_saturday_breakfast': False, 'open_saturday_lunch': True,
             'open_saturday_dinner': True, 'open_sunday_breakfast': False, 'open_sunday_lunch': False,
             'open_sunday_dinner': False},
            {'slug': 'south', 'name': 'South Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2019-12/south-servery.jpg.jpeg?itok=JVeTEsgf',
             'open_friday_dinner': True, 'open_saturday_breakfast': False, 'open_saturday_lunch': False,
             'open_saturday_dinner': False, 'open_sunday_breakfast': False, 'open_sunday_lunch': True,
             'open_sunday_dinner': True},
            {'slug': 'north', 'name': 'North Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2020-08/Rice-Brown-College_0.jpg.jpeg?itok=0YsxigYZ',
             'open_friday_dinner': True, 'open_saturday_breakfast': True, 'open_saturday_lunch': True,
             'open_saturday_dinner': True, 'open_sunday_breakfast': False, 'open_sunday_lunch': False,
             'open_sunday_dinner': True},
        ]
        for servery in serveries:
            Servery.objects.get_or_create(slug=servery['slug'], name=servery['name'], image=servery['image'],
                                          open_friday_dinner=servery['open_friday_dinner'],
                                          open_saturday_breakfast=servery['open_saturday_breakfast'],
                                          open_saturday_lunch=servery['open_saturday_lunch'],
                                          open_saturday_dinner=servery['open_saturday_dinner'],
                                          open_sunday_breakfast=servery['open_sunday_breakfast'],
                                          open_sunday_lunch=servery['open_sunday_lunch'],
                                          open_sunday_dinner=servery['open_sunday_dinner'],
                                          )
            print(servery['name'])

        dishes = [
            {'name': 'Steamed Rice', 'vegan': True, 'vegetarian': True}
        ]
        for dish in dishes:
            optional_keys = [
                'eggs',
                'fish',
                'gluten',
                'milk',
                'peanuts',
                'shellfish',
                'soy',
                'tree_nuts',
                'vegan',
                'vegetarian',
            ]
            for key in optional_keys:
                if key not in dish:
                    dish[key] = False
            Dish.objects.get_or_create(
                name=dish['name'],
                eggs=dish['eggs'],
                fish=dish['fish'],
                gluten=dish['gluten'],
                milk=dish['milk'],
                peanuts=dish['peanuts'],
                shellfish=dish['shellfish'],
                soy=dish['soy'],
                tree_nuts=dish['tree_nuts'],
                vegan=dish['vegan'],
                vegetarian=dish['vegetarian'],
            )
            print(dish['name'])

        meals = [{'servery': random.choice(list(Servery.objects.all())),
                  'meal_type': random.choice(('Breakfast', 'Lunch', 'Dinner')),
                  'meal_date': datetime.date(year=2021, month=random.randrange(8, 10), day=random.randrange(0, 30)),
                  'meal_start_time': datetime.time(hour=random.randrange(0, 12), minute=random.randrange(0, 60),
                                                   second=random.randrange(0, 60)),
                  'meal_end_time': datetime.time(hour=random.randrange(12, 24), minute=random.randrange(0, 60),
                                                 second=random.randrange(0, 60)),
                  }]
        for meal in meals:
            Meal.objects.get_or_create(
                servery=meal['servery'],
                meal_type=meal['meal_type'],
                meal_date=meal['meal_date'],
                meal_start_time=meal['meal_start_time'],
                meal_end_time=meal['meal_end_time'],
            )
            print(meal['servery'], meal['meal_type'])

        for dish in Dish.objects.all():
            DishAppearance.objects.get_or_create(dish=dish, meal=random.choice(Meal.objects.all()))
            print(f'Dish Appearance: {dish.name}')

        User.objects.get_or_create(username='Hi', password='w#$eO&oIFo8L')
        latin_words = ['Lorem',
                       'ipsum',
                       'dolor',
                       'sit',
                       'amet',
                       'Donec',
                       'vehicula',
                       'urna',
                       'a',
                       'eleifend',
                       'viverra',
                       'ex',
                       'felis',
                       'ullamcorper',
                       'metus',
                       'rutrum',
                       'turpis',
                       'nisl',
                       'in',
                       'quam',
                       'Nam',
                       'id',
                       'placerat',
                       'Aliquam',
                       'ut',
                       'turpis.',
                       'lectus',
                       'vel',
                       'tempor',
                       'auctor',
                       'at',
                       'purus',
                       'Mauris',
                       'pulvinar',
                       'tristique',
                       'tempus',
                       'tincidunt',
                       'iaculis',
                       'risus',
                       'non',
                       'mauris',
                       'sodales',
                       'Sed',
                       'vitae',
                       'est',
                       'commodo',
                       'porttitor',
                       'eget',
                       'enim',
                       'Curabitur',
                       'lorem',
                       'lacus',
                       'mattis', ]
        for dish_appearance in DishAppearance.objects.all():
            for i in range(random.randrange(1, 10)):
                user = random.choice(User.objects.all())
                Review.objects.get_or_create(
                    dish_appearance=dish_appearance,
                    user=user,
                    stars=random.randrange(1, 11),
                    review_text=' '.join(random.sample(latin_words, 15))
                )
                print(f'Dish: {dish_appearance.dish.name}, user: {user}')
