import requests

# The code below is for step 2 of the CODE2040 API Challenge

api_token = "dc9daf749ac1b14787b989fe1b97d42c"

"""
Connects to the CODE2040 challenge endpoint, sends the required
token in JSON format, and get the string back.
"""
def getStringToReverse():
    challenge_endpoint = "http://challenge.code2040.org/api/reverse"

    # Send JSON with token to the endpoint
    json = {"token" : api_token}
    response = requests.post(challenge_endpoint, data=json)
    # Read in the string that is returned from the endpoint
    stringToReverse = response.content

    return stringToReverse

"""
Sends the reversed string to the validation endpoint

String revStr - the reversed string we need to send back
"""
def sendReversedStr(revStr):
    validate_endpoint = "http://challenge.code2040.org/api/reverse/validate"
    json = {"token" : api_token,
            "string" : revStr
            }

    response = requests.post(validate_endpoint, data=json)
    print "Response from API: " + response.content



def main():
    # Retrieve the string to reverse from the endpoint
    str = getStringToReverse()
    print "The API has given us this string: " + str
    # Reverse the string
    rev = ''.join(reversed(str))
    print "Now, the reversed string is " + rev
    # Send it back to the validation endpoint
    sendReversedStr(rev)


if __name__ == "__main__":
    main()