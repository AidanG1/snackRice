from django.core.management.base import BaseCommand
from ...models import Servery


class Command(BaseCommand):
    help = 'add serveries'

    def handle(self, *args, **options):
        serveries = [
            {'slug': 'west', 'name': 'West Servery',
             'image': 'https://dining.rice.edu/sites/g/files/bxs4236/files/styles/page_hero_image/public/2019-12/west-servery_0.jpg.jpeg?itok=JC0x_3bt',
             'open_friday_dinner': True, 'open_saturday_breakfast': False, 'open_saturday_lunch': False,
             'open_saturday_dinner': False, 'open_sunday_breakfast': True, 'open_sunday_lunch': True,
             'open_sunday_dinner': True},
            {'slug': 'seibel', 'name': 'Seibel Servery',
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
