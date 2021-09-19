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
    receive_notification_time = models.IntegerField(default=30,
                                                    help_text='Time in minutes after meal start to receive notification message.')
    preference_choices = (
        ('prefer_tag', 'Prefer Tag'),
        ('no_preference', 'No Preference'),
        ('prefer_no_tag', 'Prefer No Tag'),
    )
    eggs = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    fish = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    gluten = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    milk = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    peanuts = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    shellfish = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    soy = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    tree_nuts = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    vegan = models.CharField(default='no_preference', max_length=15, choices=preference_choices)
    vegetarian = models.CharField(default='no_preference', max_length=15, choices=preference_choices)

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
