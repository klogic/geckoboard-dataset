import requests 
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
apikey = os.getenv('apikey')
if not apikey:
    print('can\'t get api key in env file')

def testconnection(apikey):
    ''' this method test requests to server '''
    url = "https://api.geckoboard.com/"
    headers = {
        "Authorization": "Basic "+apikey
    }
    response = requests.request("GET", url, headers=headers)
    return response.status_code

result = testconnection(apikey)
print result

# result status code if successfull it will return 200 otherwise error occur
