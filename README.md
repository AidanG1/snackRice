# snackrice.tech
Built in under 36 hours, Snack Rice is your go-to place for Rice University's serveries. Snack Rice illustrates the weekly menu for all serveries in a concise and easy manner. With the possibility to review all servery food, filter food based on dietary restrictions, and set up custom SMS messages to alert you of your favorite foods, Snack Rice will soon become your favorite site.

## Future Todos:
	- Add food poisoning alert
	- Adding information for calories for each meal
	- Suggests what food you should try out in your next adventure - machine learning 😉
	- See where your friends/followers are eating
		
## Techstack:
	- Django (python)
	- SQLite
	- NodeJS (javascript/html/css)
	- Twilio (sms)
	- Google Cloud (Google Maps API)
	- Domain.com

## Instructions on how to host locally

First, clone the repository.
```bash
$ git clone git@github.com/AidanG1/snackRice.git
$ cd snackRice
```
Then set up your virtual environment and install the requirements.
```
$ pip install -r requirements.txt
```
Next apply database migrations
```
$ python manage.py migrate
```
Finally, run the website on localhost. Visit localhost:8000 in your browser!
```
$ python manage.py runserver
```
	
### Made by snackrice: Aidan, Ian, Karl, and Phoebe
