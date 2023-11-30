import requests
import config


url = "https://api.yelp.com/v3/businesses/search/phone"

headers = {
  "Authorization": "Bearer " + config.yelp_api_key
}

params = {
  "phone": "+14159083801"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
for item in businesses:
 print(item["name"], "\n", item["alias"])
