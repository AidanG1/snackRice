from django.core.management.base import BaseCommand
from ...models import *
import random
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'clear dishes and meals'

    def handle(self, *args, **options):
        usernames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for username in usernames:
            if User.objects.filter(username=username).count() == 0:
                User.objects.create_user(username=username, password='P@ssword123$01t1$$3cur3')
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
        for username in usernames:
            for i in range(0, random.randrange(10, 40)):
                print(f'Username: {i}')
                Review.objects.create(
                    dish_appearance=random.choice(DishAppearance.objects.all()),
                    user=User.objects.get(username=username),
                    stars=random.randrange(1, 6),
                    review_text=' '.join(random.sample(latin_words, 15)))
