import os, django
import requests
import urllib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from main.models import Servery, Meal, DishAppearance
from users.models import Profile
from django.contrib.auth.models import User

riceu_lat = 29.717862
riceu_long = -95.402341
riceu_radius = 1600  # meters

south_servery_id = "ChIJrzkPQ3rAQIYR5G-qT8e30jw"
north_servery_id = "ChIJE6xUHX_AQIYRHXGmY2q7a1Y"
west_servery_id = "ChIJf8hcvX7AQIYRH9dtCL4HGXw"
baker_servery_id = "ChIJuXPL03vAQIYRF9i4a0IUVAE"
seibel_servery_id = "ChIJGTEMkHnAQIYREr6DQPZulXM"

google_key = os.environ['GOOGLE_PATH']


def generate_url(fields, apitype, key):
    url = "https://maps.googleapis.com/maps/api/"
    url += apitype
    url += "/json?"
    for field, value in fields.items():
        url += (urllib.parse.quote(field) + "=" + urllib.parse.quote(value) + "&")
    url += ("key=" + key)
    return url

def maps_recommendations(input):
    url = generate_url({"input": input, "strictbounds": "true", "location": str(riceu_lat) + "," + str(riceu_long),
                        "radius": str(riceu_radius)}, "place/autocomplete", key)
    response = requests.request("GET", url, headers={}, data={})
    response = response.json()
    recommendations = []
    for location in response["predictions"]:
        recommendations.append(
            {"name": location["structured_formatting"]["main_text"], "place_id": location["place_id"]})
    return recommendations

def servery_distances(place_id):
    destinations = ""
    for servery_id in [south_servery_id, north_servery_id, seibel_servery_id, west_servery_id]:
        destinations += "place_id:" + servery_id + "|"
    destinations += "place_id:" + baker_servery_id
    url = generate_url({"destinations": destinations, "origins": "place_id:" + place_id, "mode": "WALKING"},
                       "distancematrix", key)
    response = requests.request("GET", url, headers={}, data={}).json()
    times = {
        "South":response["rows"][0]["elements"][0]["duration"]["value"],
        "North":response["rows"][0]["elements"][1]["duration"]["value"],
        "Seibel":response["rows"][0]["elements"][2]["duration"]["value"],
        "West":response["rows"][0]["elements"][3]["duration"]["value"],
        "Baker":response["rows"][0]["elements"][4]["duration"]["value"]
    }
    return times

def optimized_servery_points(servery_dists, servery_scores, walking_factor):
    final_scores = {}
    max_dist = 0
    max_servery = ""
    for servery, dist in servery_dists.items():
        if dist > max_dist:
            max_dist = dist
            max_servery = servery
    for key, value in servery_dists:
        final_scores[key] = servery_scores[key] * (1 - walking_factor) + servery_dists[key] / max_dist * walking_factor

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
    for servery, meal_rating in meal_ratings.items():
        meal_ratings[servery] = meal_rating / 10.0
    servery_dists = servery_distances(maps_recommendations[0]["place_id"])
    servery_scores = optimized_servery_points(servery_dists, meal_ratings, user_profile.walking_factor)
    print(servery_scores)

if __name__ == '__main__':
    main()
