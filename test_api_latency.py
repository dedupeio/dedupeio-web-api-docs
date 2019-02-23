from time import time
import requests 
import json
from test_api_settings import API_KEY, PROJECT_ID, NUM_REQUESTS

def perform_post():
    # api-endpoint 
    URL = "https://app.dedupe.io/api/v1/match/"

    PARAMS = {
      "api_key": API_KEY,
      "project_id": PROJECT_ID,
      "object": {
        "site_name": "Korean American Community Services",
        "address": "4300 North California Ave.   60618",
        "phone": "5838281",
        "fax": ""
      },
      "threshold": 0.8
    } 
      
    # sending get request and saving the response as response object 
    r = requests.post(url = URL, json = PARAMS)
      
    # extracting data in json format 
    data = r.json()

if __name__ == '__main__':
    print('starting api calls')
    time_before = time()
    for x in range(0, NUM_REQUESTS):
        perform_post()
    time_after = time()
    time_taken = time_after-time_before
    avg_response_time = time_taken / NUM_REQUESTS

    print('%s API calls completed' % NUM_REQUESTS)
    print('%s seconds elapsed' % time_taken)
    print("average response time: %s" % avg_response_time)