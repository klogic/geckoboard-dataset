import requests 


def testconnection(apikey):''' this method test requests to server '''
    url = "https://api.geckoboard.com/"
    headers = {
        "Authorization": "Basic "+apikey
    }
    response = requests.request("GET", url, headers=headers)
    return response.status_code

result = testconnection('<you-api-key->')
print result

# result status code if successfull it will return 200 otherwise error occur
