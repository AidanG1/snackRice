from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.db.models import Avg
import datetime


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

    @property
    def current_meal(self):
        meals = Meal.objects.filter(servery=self, meal_date=datetime.date.today())
        for meal in meals:
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


class DishAppearance(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    @property
    def reviews(self):
        return Review.objects.filter(dish_appearance=self)

    @property
    def average_stars(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg']

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def overall_star_list(self):
        appearances = DishAppearance.objects.filter(dish=self.dish)
        stars_list = []
        for appearance in appearances:
            reviews = Review.objects.filter(dish_appearance=appearance)
            stars_list += reviews.values_list('stars')
        return stars_list

    @property
    def overall_rating_count_average(self):
        stars_list = self.overall_star_list
        return {'average': sum(stars_list) / len(stars_list), 'count': len(stars_list)}


class Review(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    dish_appearance = models.ForeignKey(DishAppearance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    review_datetime = models.DateTimeField(auto_now_add=True)
    review_text = models.TextField(null=True, blank=True)
