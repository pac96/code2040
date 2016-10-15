import requests

# The code below is for step 4 of the CODE2040 API Challenge
# I've decided that since these are just supposed to be quick Python
# scripts, I won't do all of the boilerplate and make a main method
# and helper functions

api_token = "dc9daf749ac1b14787b989fe1b97d42c"
challenge_endpoint = "http://challenge.code2040.org/api/prefix"
validation_endpoint = "http://challenge.code2040.org/api/prefix/validate"
ret_list = []


# Post token to endpoint
json = {"token" : api_token}
res = requests.post(challenge_endpoint, data=json)
json_dict = res.json();


# Get the prefix and the array from the json dictionary
prefix = json_dict.get("prefix")
prefix_len = len(prefix)
arr = json_dict.get("array")


# Get the elements that do not have the specified prefix in the array
for elt in arr:
	if elt[:prefix_len] != prefix:
		ret_list.append(elt)


# Validate your array by sending it back to the validation endpoint
ret_json = {"token" : api_token, "array" : ret_list}
finalResponse = requests.post(validation_endpoint, json=ret_json)