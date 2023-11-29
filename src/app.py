import os
import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = os.environ.get("yelp_api_key")
headers = {
  "authorization": "Bearer " + api_key
}
params = {
  "term": "Barber",
  "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)
