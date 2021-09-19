# snackrice.tech
Built in under 36 hours, Snack Rice is your go-to place for Rice University's serveries. Snack Rice illustrates the weekly menu for all serveries in a concise and easy manner. With the possibility to review all servery food, filter food based on dietary restrictions, and set up custom SMS messages to alert you of your favorite foods, Snack Rice will soon become your favorite site.

## Feature List:
	- Automated tasks to scrape meal information from dining.rice.edu
	- Customized meal text notifications using the Twilio API and a Node.js server
		- Dietary restrictions (vegan, vegetarian, gluten free, and more)
		- Proximity from serveries (Google Maps API)
		- Reviews of dishes
		- Notification timing
	- Review every dish with star rating and review text
	- Option for crowdsourcing data and images if Rice website is incorrect
	- Infinite scroll leaderboard of users with the most reviews
	- Infinite scroll leaderboard of dishes with the best reviews
	- Persistent light/dark themes based off user choice and browser settings
	
## 15 Simple Steps to Communicate Between Text, Django, Flask, and Google Maps
	1. User sets up account with Snack Rice
	2. User puts in phone number, preferences about walking and food quality, dietary restrictions, and notification timing
	3. Django timed task calls notification loop
	4. Django calls Google Maps API to determine distances between serveries and default locations
	5. Django determines the best choice based on distances, reviews, and restrictions
	6. Django sends the best servery choice and menu
	7. If user is not in default location, user responds to text
	8. Flask server reads text
	9. Flask server sends request to Google Maps API
	10. Flask texts user detailed location choices based on their input
	11. User responds to text with one of the location choices
	12. Flask sends text to django with user info and location choice
	13. Django calls Google Maps API to get distances
	14. Django determines the best choice based on distances, reviews, and restrictions
	15. Django sends text with Twilio to user
	
## Future Todos:
	- Add food poisoning alert
	- Adding information for calories for each meal
	- Suggests what food you should try out in your next adventure - machine learning 😉
	- See where your friends/followers are eating
		
## Techstack:
	- Django (python)
	- Django templates (html/css/js/python)
	- SQLite
	- NodeJS (html/css/js)
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
```bash
$ pip install -r requirements.txt
```
Next apply database migrations
```bash
$ python manage.py migrate
```
Finally, run the website on localhost. Visit localhost:8000 in your browser!
```bash
$ python manage.py runserver
```
	
### Made by snackrice: Aidan, Ian, Karl, and Phoebe
