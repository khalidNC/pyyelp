import os
import requests

# Store the yelp search endpoint in a variable 
url = "https://api.yelp.com/v3/businesses/search"

# Use python environment variable, os module get method retrives yelp_api_key from local and store in api_key variable 
api_key = os.environ.get("yelp_api_key")

# Dictionary with key: value to authenticate the yelp api to tell who we are
headers = {
  "authorization": "Bearer " + api_key
}

# Dictionary that has key: value to filter by location that is required
params = {
  "term": "Barber",
  "location": "NYC"
}

# Request to get the endpoint to yelp api and store the result in presponse object
response = requests.get(url, headers=headers, params=params)

# Call the json method to the response that return list of dictionaries and immideatly access by the key businesses
businesses = response.json()["businesses"]

# Make list comprehention item for item in iterable then filter; check if the business has a rating number 4.5 or more and get them 
names = [business["name"] for business in businesses if business["rating"] > 4.5]

# Finally print the result
print(names)
