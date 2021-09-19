from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from main.models import Review


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    walking_factor = models.IntegerField(default=5)
    food_factor = models.IntegerField(default=5)

    @property
    def reviews(self):
        return Review.objects.filter(user=self.user)

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def average_stars(self):
        reviews = Review.objects.filter(user=self.user)
        stars_list = reviews.values_list('stars', flat=True)
        if len(stars_list) == 0:
            return 0
        else:
            return sum(stars_list) / len(stars_list)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
