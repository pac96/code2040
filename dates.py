import requests

# The code below is for step 4 of the CODE2040 API Challenge
# I've decided that since these are just supposed to be quick Python
# scripts, I won't do all of the boilerplate and make a main method
# and helper functions

api_token = "dc9daf749ac1b14787b989fe1b97d42c"
challenge_endpoint = "http://challenge.code2040.org/api/dating"
validation_endpoint = "http://challenge.code2040.org/api/dating/validate"
ret_list = []


# Post token to endpoint
token_json = {"token" : api_token}
res = requests.post(challenge_endpoint, data=token_json)
print "Date:", res.content


# Validate your array by sending it back to the validation endpoint
# ret_json = {"token" : api_token, "datestamp" : ret_list}
# finalResponse = requests.post(validation_endpoint, json=ret_json)