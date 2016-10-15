import requests

# Step 3 of CODE2040 API Challenge

api_token = "dc9daf749ac1b14787b989fe1b97d42c"

"""
Retrieves the needle and array from the haystack endpoint

String endpoint - the endpoint to retrieve the data from

Returns a dictionary with the needle and the haystack array
"""
def getNeedleAndArray(endpoint):
    encoded_data = {'token' : api_token}
    response = requests.post(endpoint, data=encoded_data)
    response_dict = response.json()

    return response_dict

"""
Finds the index of the input needle in the haystack

String needle - the needle we need to find
List haystack - a list of strings that we need to search through

Returns the index of the needle within the haystack
"""
def findNeedleIndex(needle, haystack):
    index = None
    if (needle in haystack):
        index = haystack.index(needle)

    return index

def main():
    haystack_endpoint = "http://challenge.code2040.org/api/haystack"
    validation_endpoint = "http://challenge.code2040.org/api/haystack/validate"

    # Retrieve the haystack and needle from the API endpoint
    endpoint_dict = getNeedleAndArray(haystack_endpoint)
    needle = endpoint_dict.get("needle")
    haystack = endpoint_dict.get("haystack")

    # Find the index of the needle in the haystack
    index = findNeedleIndex(needle, haystack)
    json = {"token" : api_token, "needle" : index}

    # Send that index to the validation endpoint
    r = requests.post(validation_endpoint, data=json)

if __name__ == "__main__":
    main()
