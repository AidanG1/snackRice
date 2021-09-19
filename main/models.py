from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.db.models import Avg
import datetime


def current_meal_models():
    int_to_day = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    day = int_to_day[datetime.datetime.today().weekday()]
    if datetime.datetime.now().time().hour < 10 or (
            datetime.datetime.now().time().hour == 10 and datetime.datetime.now().time().minute <= 30):
        meal = 'Breakfast'
    elif datetime.datetime.now().time().hour <= 14 and datetime.datetime.now().time().minute <= 0:
        meal = 'Lunch'
    else:
        meal = 'Dinner'
    return f'{day} {meal}'


class Servery(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=40)
    image = models.URLField(max_length=250)
    open_friday_dinner = models.BooleanField(default=True)
    open_saturday_breakfast = models.BooleanField(default=True)
    open_saturday_lunch = models.BooleanField(default=True)
    open_saturday_dinner = models.BooleanField(default=True)
    open_sunday_breakfast = models.BooleanField(default=True)
    open_sunday_lunch = models.BooleanField(default=True)
    open_sunday_dinner = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Serveries'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def open_now(self):
        if current_meal_models() == 'Friday Dinner':
            return self.open_friday_dinner
        elif current_meal_models() == 'Saturday Breakfast':
            return self.open_saturday_breakfast
        elif current_meal_models() == 'Saturday Lunch':
            return self.open_saturday_lunch
        elif current_meal_models() == 'Saturday Dinner':
            return self.open_saturday_dinner
        elif current_meal_models() == 'Sunday Breakfast':
            return self.open_sunday_breakfast
        elif current_meal_models() == 'Sunday Lunch':
            return self.open_sunday_lunch
        elif current_meal_models() == 'Sunday Dinner':
            return self.open_sunday_dinner
        else:
            return True

    @property
    def current_meal(self):
        meals = Meal.objects.filter(servery=self, meal_date=datetime.date.today())
        for meal in meals.order_by('-meal_end_time'):
            if datetime.datetime.now().time() <= meal.meal_end_time:
                return meal
        return meals.last()

    @property
    def current_dishes(self):
        return DishAppearance.objects.filter(meal=self.current_meal)


class Dish(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=250, blank=True, null=True)
    eggs = models.BooleanField(default=False)
    fish = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    shellfish = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    tree_nuts = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Meal(models.Model):
    meal_choices = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    uuid = ShortUUIDField(primary_key=True)
    servery = models.ForeignKey(Servery, on_delete=models.CASCADE)
    meal_type = models.CharField(choices=meal_choices, max_length=10)
    meal_date = models.DateField()
    meal_start_time = models.TimeField()
    meal_end_time = models.TimeField()

    def __str__(self):
        return f'{self.servery.name} {self.meal_type} on {self.meal_date.strftime("%b %d, %Y")}'


class DishAppearance(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish} {self.meal}'

    @property
    def reviews(self):
        return Review.objects.filter(dish_appearance=self)

    @property
    def average_stars(self):
        avg = self.reviews.aggregate(Avg('stars'))['stars__avg']
        if isinstance(avg, type(None)):
            return 0
        else:
            return avg

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def overall_star_list(self):
        appearances = DishAppearance.objects.filter(dish=self.dish)
        stars_list = []
        for appearance in appearances:
            reviews = Review.objects.filter(dish_appearance=appearance)
            stars_list += reviews.values_list('stars', flat=True)
        return stars_list

    @property
    def overall_rating_count_average(self):
        stars_list = self.overall_star_list
        return_dict = {'count': len(stars_list)}
        if len(stars_list) == 0:
            return_dict['average'] = 0
        else:
            return_dict['average'] = sum(stars_list) / len(stars_list)
        return return_dict


class Review(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    dish_appearance = models.ForeignKey(DishAppearance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    review_datetime = models.DateTimeField(auto_now_add=True)
    review_text = models.TextField(null=True, blank=True)
