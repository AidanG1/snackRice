from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile
from ...models import *


class Command(BaseCommand):
    help = 'utility command'

    def handle(self, *args, **options):
        s = Servery.objects.get(slug='Seibel')
        s.slug = 'seibel'
        s.name = 'Seibel Servery'
        s.save()
