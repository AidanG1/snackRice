import os
import logging
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
msg_service_sid = os.environ['TWILIO_MSG_SERVICE_SID']

client = Client(account_sid, auth_token)
app = Flask(__name__)

callers = {
    "+16469401926": "Karl",
}



def send_message(message: str, to_phone_number: str):
    message = client.messages.create(
        messaging_service_sid=msg_service_sid,
        body=message,
        to=to_phone_number
    )
    logging.warning(message.sid)


@app.route("/")
def check_app():
    # returns a simple string stating the app is working
    return Response("Welcome to SnackRice's project"), 200


@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    number = request.form['From']
    message_body = request.form['Body']

    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)


if __name__ == '__main__':
    app.run(port=5050)
