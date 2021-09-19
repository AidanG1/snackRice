import os
import logging
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
msg_service_sid = os.environ['TWILIO_MSG_SERVICE_SID']

client = Client(account_sid, auth_token)


def send_message(message: str, to_phone_number: str):
    message = client.messages.create(
        messaging_service_sid=msg_service_sid,
        body=message,
        to=to_phone_number
    )
    logging.warning(message.sid)


send_message("Hello ian v2", "+19713525393")
