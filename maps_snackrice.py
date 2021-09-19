import requests
import urllib
import os

riceu_lat = 29.717862
riceu_long = -95.402341
riceu_radius = 1600  # meters

south_servery_id = "ChIJrzkPQ3rAQIYR5G-qT8e30jw"
north_servery_id = "ChIJE6xUHX_AQIYRHXGmY2q7a1Y"
west_servery_id = "ChIJf8hcvX7AQIYRH9dtCL4HGXw"
baker_servery_id = "ChIJuXPL03vAQIYRF9i4a0IUVAE"
seibel_servery_id = "ChIJGTEMkHnAQIYREr6DQPZulXM"

# [south, north, seibel, west, baker]
servery_indices = {0: "South", 1: "North", 2: "Seibel", 3: "West", 4: "Baker"}
test_servery_scores = [0.90, 0.20, 0.23, 0.21, 0.27]  # 1.0 is the best food ever, 0.0 is dogshit
walking_factor = 0.1  # 1.0 is "id rather die than walk", 0.0 is "im a sigma male athlete"

key = os.environ['GOOGLE_PATH']


def generate_url(fields, apitype, key):
    url = "https://maps.googleapis.com/maps/api/"
    url += apitype
    url += "/json?"
    for field, value in fields.items():
        url += (urllib.parse.quote(field) + "=" + urllib.parse.quote(value) + "&")
    url += ("key=" + key)
    return url


# print(generate_url({"place_id":north_servery_id,"fields":"name"},"details",key))

def maps_recommendations(input):
    url = generate_url({"input": input, "strictbounds": "true", "location": str(riceu_lat) + "," + str(riceu_long),
                        "radius": str(riceu_radius)}, "place/autocomplete", key)
    response = requests.request("GET", url, headers={}, data={})
    response = response.json()
    recommendations = []
    for location in response["predictions"]:
        recommendations.append(
            {"name": location["structured_formatting"]["main_text"], "place_id": location["place_id"]})
    return recommendations


def servery_distances(place_id):
    destinations = ""
    for servery_id in [south_servery_id, north_servery_id, seibel_servery_id, west_servery_id]:
        destinations += "place_id:" + servery_id + "|"
    destinations += "place_id:" + baker_servery_id
    url = generate_url({"destinations": destinations, "origins": "place_id:" + place_id, "mode": "WALKING"},
                       "distancematrix", key)
    response = requests.request("GET", url, headers={}, data={}).json()
    times = []
    print(response["rows"][0]["elements"])
    for stat in response["rows"][0]["elements"]:
        times.append(stat["duration"]["value"])

    return times


def optimized_servery(servery_dists, servery_scores, walking_factor):
    servery_better_scores = []
    max_dist = 0
    for dist in servery_dists:
        if dist > max_dist:
            max_dist = dist
    for i in range(len(servery_dists)):
        servery_better_scores.append(
            -1 * servery_dists[i] / max_dist * walking_factor + servery_scores[i] * (1 - walking_factor))
    max_score_and_index = (0, 0)
    for i in range(len(servery_better_scores)):
        if servery_better_scores[i] > max_score_and_index[0]:
            max_score_and_index = (servery_better_scores[i], i)
    return max_score_and_index[1]


map_recs = maps_recommendations(input("Search for recommendations: "))
for rec in map_recs:
    print(rec["name"])
chosen_location = map_recs[int(input("Which number? ")) - 1]
print(chosen_location["name"])
servery_dists = servery_distances(chosen_location["place_id"])
print("")
print("The best servery is " + servery_indices[optimized_servery(servery_dists, test_servery_scores, walking_factor)])
