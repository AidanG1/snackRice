import os, django
from twilio.rest import Client
from findbestservery import main as fbs_main
from findbestservery import maps_recommendations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snackRice.settings")
django.setup()

from django.contrib.auth.models import User
from main.models import Servery


def main():
    account_sid = 'AC0c783578746935f45f42a31c9ec25c41'
    auth_token = 'aa0feca13ff23597808584b6f9c0dd9f'
    msg_service_sid = 'MG90cf15a73db3661df5599417d983be27'

    client = Client(account_sid, auth_token)

    max_value = -100
    correct_key = ''
    print(maps_recommendations(User.objects.get(
                username='Superuser').profile.default_location)[
                0])
    for key, value in fbs_main(
            maps_recommendations(User.objects.get(
                username='Superuser').profile.default_location)[0][
                'place_id']).items():
        if value > max_value:
            max_value = value
            correct_key = key
    current_dishes = Servery.objects.get(name=correct_key).current_dishes
    message_string = f'Your recommended servery is {correct_key}'
    for dish in [{'dish': dish.dish.name, 'stars': dish.average_stars, 'reviews': dish.review_count}
                 for dish in current_dishes]:
        message_string += f"\n{dish['dish']}, {dish['stars']}/5 with {dish['reviews']} reviews"

    def send_message(message: str):
        message = client.messages.create(
            messaging_service_sid=msg_service_sid,
            body=message,
            to='+19713525393'
        )
    send_message(message_string)


if __name__ == '__main__':
    main()
