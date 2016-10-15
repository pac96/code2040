import urllib
import urllib2

api_token = "dc9daf749ac1b14787b989fe1b97d42c"
repository = "https://github.com/pac96/code2040-challenge"

"""
Connects to the CODE2040 challenge endpoint and sends the required
data in JSON format. 

For step 1 of the CODE2040 API Challenge
"""
def connect():
    # Connect to the challenge endpoint
    challenge_endpoint = "http://challenge.code2040.org/api/register"

    # Send JSON with token and github repository
    json = {"token" : api_token, 
            "github" : repository}
    data = urllib.urlencode(json)
    req = urllib2.Request(challenge_endpoint, data)
    response = urllib2.urlopen(req)
    print "Response from API: " + response.read()



def main():
    connect()



if __name__ == "__main__":
    main()