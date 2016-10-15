import requests
import arrow

# The code below is for step 4 of the CODE2040 API Challenge
# I've decided that since these are just supposed to be quick Python
# scripts, I won't do all of the boilerplate and make a main method
# and helper functions

api_token = "dc9daf749ac1b14787b989fe1b97d42c"
challenge_endpoint = "http://challenge.code2040.org/api/dating"
validation_endpoint = "http://challenge.code2040.org/api/dating/validate"


# Post token to endpoint and retrieve the datestamp and interval
token_json = {"token" : api_token}
res = requests.post(challenge_endpoint, data=token_json)
challenge_json = res.json()
datestamp = challenge_json["datestamp"]
interval = challenge_json["interval"]

# Add the interval to the date
arrow_date = arrow.get(datestamp)
# Get the date in seconds and add it to the interval
new_date_timestamp = interval + arrow_date.timestamp

# Convert the new date (now in seconds) back to UTC
final_utc_date = arrow.Arrow.utcfromtimestamp(new_date_timestamp).format("YYYY-MM-DDTHH:mm:ss") + "Z"

# Validate your array by sending it back to the validation endpoint
ret_json = {"token" : api_token, "datestamp" : final_utc_date}
finalResponse = requests.post(validation_endpoint, json=ret_json)