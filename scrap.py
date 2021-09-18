import datetime

from bs4 import BeautifulSoup
import os, django, requests, js2py

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from main.models import Servery, Meal, Dish, DishAppearance

urls = ["https://websvc-aws.rice.edu:8443/static-files/dining-assets/Baker-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/West-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/Seibel-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/North-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/South-Servery-Menu-Full-Week.js"]


def scrap_weekly_menu(url: str):
    # The first part is to get the static file with the javascript quote that
    # has the data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # now we can load that function as javascript and get the result in python
    function = js2py.eval_js(soup.text)
    # we need to make sure the name corresponds to the right function
    servery_name = url[60:url.find("-Servery")]
    html_result = function(f"{servery_name.lower()}ServeryMenuFullWeekTemplate")
    # now we can start scarping the data for real
    soup = BeautifulSoup(html_result, "html.parser")

    # The format will be as such:
    # {"Day": {"Lunch": {"meal": ["Restrictions1", "Restrictions2"]},
    #        "Dinner": {"meal": ["Restrictions"]}}}
    # I wanted to automate this, so where are getting the dates as well

    meal_index = {}
    menu_options = soup.findAll("table", attrs="menu-items")
    for (index, option) in enumerate(menu_options):
        rows = option.findAll('td')
        meals = []
        for row in rows:
            current_meal = {}
            meal = row.find("div", attrs={"class": "mitem"}).get_text()
            icons = []
            for icon in row.findAll(class_=True)[1:]:
                check = icon["class"][2][6:]
                icons.append(check)
            current_meal['name'] = meal
            current_meal['icons'] = icons
            meals.append(current_meal)
        meal_index[index] = meals
    return meal_index


if __name__ == "__main__":
    # this assumes that it will be ran on a Monday at midnight
    for url in urls:
        print('Starting:', url)
        menu = scrap_weekly_menu(url)
        servery = Servery.objects.get(slug=url.split('/')[5].split('-')[0].lower())
        for i in range(0, 7):
            meal_date = datetime.datetime.today() + datetime.timedelta(days=i)
            meal_end_time = datetime.time(hour=10, minute=30, second=0)
            if i >= 5:
                meal_start_time = datetime.time(hour=8, minute=0, second=0)
            else:
                meal_start_time = datetime.time(hour=7, minute=30, second=0)
            meal = Meal.objects.get_or_create(
                servery=servery,
                meal_type='Breakfast',
                meal_date=meal_date,
                meal_start_time=meal_start_time,
                meal_end_time=meal_end_time,
            )[0]
            dishes = [
                Dish.objects.get_or_create(
                    name='Scrambled Eggs', eggs=True, vegetarian=True
                )[0],
                Dish.objects.get_or_create(
                    name='Biscuits and Gravy', gluten=True, vegetarian=True
                )[0],
                Dish.objects.get_or_create(
                    name='Sausage', eggs=True
                )[0],
                Dish.objects.get_or_create(
                    name='Turkey Sausage', eggs=True
                )[0],
                Dish.objects.get_or_create(
                    name='Vegan Sausage', vegan=True
                )[0],
                Dish.objects.get_or_create(
                    name='Bacon', vegan=True
                )[0],
                Dish.objects.get_or_create(
                    name='Vegan Tacos', vegan=True
                )[0],
                Dish.objects.get_or_create(
                    name='Breakfast Tacos', vegan=True
                )[0],
                Dish.objects.get_or_create(
                    name='Fruit', vegan=True
                )[0],
            ]
            for dish in dishes:
                DishAppearance.objects.get_or_create(
                    dish=dish,
                    meal=meal
                )
        for i in range(14):
            if i < 7:
                meal_type = 'Lunch'
                meal_start_time = datetime.time(hour=11, minute=30, second=0)
                meal_end_time = datetime.time(hour=14, minute=0, second=0)
            else:
                meal_type = 'Dinner'
                meal_start_time = datetime.time(hour=17, minute=0, second=0)
                meal_end_time = datetime.time(hour=19, minute=30, second=0)
            meal_date = datetime.datetime.today() + datetime.timedelta(days=i)
            meal = Meal.objects.get_or_create(servery=servery, meal_type=meal_type, meal_date=meal_date,
                                              meal_start_time=meal_start_time, meal_end_time=meal_end_time)[0]
            dishes = menu[i]
            for dish in dishes:
                dish_icons_dict = {}
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
                    if key not in dish['icons']:
                        dish_icons_dict[key] = False
                    else:
                        dish_icons_dict[key] = True
                dish_object = Dish.objects.get_or_create(
                    name=dish['name'],
                    eggs=dish_icons_dict['eggs'],
                    fish=dish_icons_dict['fish'],
                    gluten=dish_icons_dict['gluten'],
                    milk=dish_icons_dict['milk'],
                    peanuts=dish_icons_dict['peanuts'],
                    shellfish=dish_icons_dict['shellfish'],
                    soy=dish_icons_dict['soy'],
                    tree_nuts=dish_icons_dict['tree_nuts'],
                    vegan=dish_icons_dict['vegan'],
                    vegetarian=dish_icons_dict['vegetarian'],
                )[0]
                DishAppearance.objects.create(meal=meal, dish=dish_object)
