Python example
==============

This example sends one record to the :doc:`match <Endpoints>` endpoint and prints out the resulting matches.

.. code-block:: python 

  import requests
  import json
   
  # set your session IDs
  API_KEY = 'YOUR API KEY'
  PROJECT_ID = 'YOUR PROJECT ID'
   
  # the field names in the match_object must match the field names in your session
  match_object = {
    "name": 'john smith',
    "address": '222 W Merchandise Mart Plz, Chicago IL',
    "phone": "(555) 725-0195"
  }
   
  # post the
  post_data = {
    'api_key': API_KEY,
    'project_id': PROJECT_ID,
    'threshold': 0.5, # set this to a value between 0 and 1 for how conservative the returned matches should be
    'object': match_object
  }
   
  r = requests.post('https://app.dedupe.io/match/',
  data=json.dumps(post_data))
   
  # print the response from Dedupe.io
  print(r.json())