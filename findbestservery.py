import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from main.models import Servery, Meal, DishAppearance
from users.models import Profile
from django.contrib.auth.models import User


def main():
    current_meals = [servery.current_meal for servery in Servery.objects.all()]
    user_profile = User.objects.get(username='Superuser').profile
    user_preferences = {
                           'eggs': user_profile.eggs,
                           'fish': user_profile.fish,
                           'gluten': user_profile.gluten,
                           'milk': user_profile.milk,
                           'peanuts': user_profile.peanuts,
                           'shellfish': user_profile.shellfish,
                           'soy': user_profile.soy,
                           'tree_nuts': user_profile.tree_nuts,
                           'vegan': user_profile.vegan,
                           'vegetarian': user_profile.vegetarian
                       }
    for key, value in user_preferences.copy().items():
        if value == 'no_preference':
            user_preferences.pop(key)
    meal_ratings = {}
    for meal in current_meals:
        meal_ratings[meal.servery.name] = 0
        dishes = DishAppearance.objects.filter(meal=meal)
        for dish in dishes:
            for key, value in user_preferences.items():
                if key == 'eggs':
                    if DishAppearance.dish.eggs != value:
                        continue
                elif key == 'fish':
                    if DishAppearance.dish.fish != value:
                        continue
                elif key == 'gluten':
                    if DishAppearance.dish.gluten != value:
                        continue
                elif key == 'milk':
                    if DishAppearance.dish.milk != value:
                        continue
                elif key == 'peanuts':
                    if DishAppearance.dish.peanuts != value:
                        continue
                elif key == 'shellfish':
                    if DishAppearance.dish.shellfish != value:
                        continue
                elif key == 'soy':
                    if DishAppearance.dish.soy != value:
                        continue
                elif key == 'tree_nuts':
                    if DishAppearance.dish.tree_nuts != value:
                        continue
                elif key == 'vegan':
                    if DishAppearance.dish.vegan != value:
                        continue
                elif key == 'vegetarian':
                    if DishAppearance.dish.vegetarian != value:
                        continue
            meal_ratings[meal.servery.name] += dish.average_stars * dish.review_count + 0.25 * (
                    dish.overall_rating_count_average['count'] * dish.overall_rating_count_average['average'])
    print(meal_ratings)


if __name__ == '__main__':
    main()
