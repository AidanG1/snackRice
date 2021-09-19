import os
import googlemaps
from flask import Flask, request, Response, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from findbestservery import maps_recommendations
from basic_send import main, account_sid, auth_token, msg_service_sid

client = Client(account_sid, auth_token)
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_KEY'))
app = Flask(__name__)
app.secret_key = os.urandom(32)
app.config.from_object(__name__)

callers = {
    "+16469401926": "Karl",
}


def send_message(message: str, to_phone_number: str):
    message = client.messages.create(
        messaging_service_sid=msg_service_sid,
        body=message,
        to=to_phone_number
    )
    # logging.warning(message.sid)


def auto_send(to_phone_number: str):
    send_message(
        "Respond to this text to input your general location", to_phone_number)


# auto_send("+16469401926")

@app.route("/")
def check_app():
    # returns a simple string stating the app is working
    return Response("Welcome to SnackRice's project"), 200


@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    number = request.form['From']

    counter = session.get("counter", 0)
    counter += 1
    session['counter'] = counter

    waiting_for_a_number = session.get("flag", False)
    session['flag'] = waiting_for_a_number

    results = session.get("results", [])
    session["results"] = results

    message_body = request.form['Body'].strip()

    while not waiting_for_a_number:
        results = maps_recommendations(message_body)
        session["results"] = results
        results = [key["name"] for key in results]
        if len(results) != 0:
            waiting_for_a_number = True
            session['flag'] = waiting_for_a_number
        else:
            continue
        msg = f"Hello, based on your input here are the first few choices\n"
        for (index, result) in enumerate(results):
            msg += str(index + 1) + ". " + result + "\n"
        resp.message(msg)
        return str(resp)

    if waiting_for_a_number:
        choice = int(message_body) - 1
        results = session.get("results")
        waiting_for_a_number = False
        session['flag'] = waiting_for_a_number
        resp.message("We got your response. Your current location is: " + results[choice]["name"])
        # send it to django
        main(results[choice]['name'])
    return str(resp)


if __name__ == '__main__':
    app.run(port=5050, debug=True)
