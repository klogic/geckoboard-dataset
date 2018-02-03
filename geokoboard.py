import requests 
import os
from dotenv import load_dotenv
import json

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

# result = testconnection(apikey)
# print result
# result status code if successfull it will return 200 otherwise error occur

def createdataset(apikey, id, payload):
    ''' this method will create dataset in geokoboard '''
    url = "https://api.geckoboard.com/datasets/"+id
    headers = {
        "Authorization": "Basic "+apikey,
        "Content-Type": "application/json"
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.status_code

payload = {
    "fields": {
        "timestamp":{
            "type": "datetime",
            "name": "Date"
        },
        "ordernumber":{
            "type": "string",
            "name": "Order Number"
        },
        "total":{
            "type": "number",
            "name": "Total"
        }
    },
  "unique_by": ["timestamp"]
}

# payload = json.dumps(payload)
# result = createdataset(apikey,'saleorder', payload)
# print result
# 201 status will return if dataset successful created

def appenddata(apikey, id, payload):
    ''' this method will append data into dataset '''
    url = "https://api.geckoboard.com/datasets/" + id + "/data"
    headers = {
        "Authorization": "Basic "+apikey,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code


payload = {
  "data": [
    {
      "timestamp": "2018-01-01T12:00:00Z",
      "ordernumber": "th_00001",
      "total": 819
    },
    {
      "timestamp": "2018-01-02T12:00:00Z",
      "ordernumber": "th_00002",
      "total": 409
    },
    {
      "timestamp": "2018-01-03T12:00:00Z",
      "ordernumber": "th_00003",
      "total": 164
    }
  ]
}

payload = json.dumps(payload)
result = appenddata(apikey,'saleorder', payload)
print result
# 200 status will return if append data successful.