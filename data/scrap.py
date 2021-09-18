import requests
from bs4 import BeautifulSoup
import js2py

urls = ["https://websvc-aws.rice.edu:8443/static-files/dining-assets/Baker-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/West-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/Seibel-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/North-Servery-Menu-Full-Week.js",
        "https://websvc-aws.rice.edu:8443/static-files/dining-assets/South-Servery-Menu-Full-Week.js"]



def scrap_weekly_menu(url: str):
    # The first part is to get the static file with the javascript quote that
    # has the data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # now we can load that function as javascript and get the result in python
    function = js2py.eval_js(soup.text)
    # we need to make sure the name corresponds to the right function
    servery_name = url[60:url.find("-Servery")]
    html_result = function(f"{servery_name.lower()}ServeryMenuFullWeekTemplate")
    # now we can start scarping the data for real
    soup = BeautifulSoup(html_result, "html.parser")

    # The format will be as such:
    # {"Day": {"Lunch": {"meal": ["Restrictions1", "Restrictions2"]},
    #        "Dinner": {"meal": ["Restrictions"]}}}
    weekly_menu = {}
    # I wanted to automate this, so where are getting the dates as well
    days = soup.findAll("div", attrs={"class":"title"})
    days = [day.get_text().strip() for day in days]

    meal_index = {}
    menu_options = soup.findAll("table", attrs="menu-items")
    for (index, option) in enumerate(menu_options):
        rows = option.findAll('td')
        meals = []
        for row in rows:
            current_meal = {}
            meal = row.find("div", attrs={"class": "mitem"}).get_text()
            icons = []
            for icon in row.findAll(class_=True)[1:]:
                check = icon["class"][2][6:]
                icons.append(check)
            current_meal[meal] = icons
            meals.append(current_meal)
        meal_index[index] = meals
    return meal_index
    # print(meal_index)
    # lunch_monday = options[0].get_text()
    # print(lunch_monday)
    # print(days[:14])
    # for lunch_days in days[:7]:
    #     weekly_menu["lunch"] =
    # print(len(days))
    # for day in days:
    #     print(days)
    # for option in options:
    #     print(option)
    # print(soup)


    # menu = soup.findAll("div", attrs={"class": "options"})
    # for option in menu:
    #     print(option)
    # print(response)



# scrap_weekly_menu(urls[0])

if __name__ == "__main__":
    for url in urls:
        print(scrap_weekly_menu(url))
