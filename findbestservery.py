import os, Django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from main.models import Servery, Meal, DishAppearance
from users.models import Profile
from django.contrib.auth.models import User

def main():
    current_meals = [servery.current_meal for servery in Servery.objects.all()]
    user_profile = User.objects.get(username='Superuser').profile



if __name__ == '__main__':
    main()
