from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile


class Command(BaseCommand):
    help = 'add a basic database'

    def handle(self, *args, **options):
        for user in User.objects.all():
            Profile.objects.get_or_create(user=user)
