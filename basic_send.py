import os, django
from twilio.rest import Client

from findbestservery import main as fbs_main
from findbestservery import maps_recommendations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from django.contrib.auth.models import User
from main.models import Servery

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
msg_service_sid = os.getenv('msg_service_sid')


def main(default_location):
    client = Client(account_sid, auth_token)

    max_value = -100
    correct_key = ''
    if len(default_location) == 0:
        default_location = User.objects.get(
            username='Superuser').profile.default_location
    for key, value in fbs_main(
            maps_recommendations(default_location)[0][
                'place_id']).items():
        if value > max_value:
            max_value = value
            correct_key = key
    current_dishes = Servery.objects.get(name=correct_key).current_dishes
    message_string = f'Your recommended servery is {correct_key}. The meal for today is: '
    for dish in [{'dish': dish.dish.name, 'stars': dish.average_stars, 'reviews': dish.review_count}
                 for dish in current_dishes]:
        message_string += f"\n{dish['dish']}, {dish['stars']}/5"
    message_string += f'\nIf you are not at your default location, {default_location}, reply with your current location'

    def send_message(message: str):
        message = client.messages.create(
            messaging_service_sid=msg_service_sid,
            body=message,
            to=os.getenv('phone_number')
        )

    send_message(message_string)


if __name__ == '__main__':
    main('')
