===========================
Dedupe.io API documentation 
===========================

Overview
========
Dedupe.io is a a software as a service  platform for quickly and accurately identifying clusters of similar records across one or more files or databases. 

When to use the API
===================
Once you have completed the de-duping process for a dataset, you can continue to incrementally check, match and add to it via API calls. 
 
By posting a chunk of data to the API (described in the **match** endpoint), dedupe.io can compare it to your dataset and return one or more potential matches. In the case where more than one result is returned, you can optionally tell dedupe.io which one is correct and it will update the training for your dataset based on it (described in the **train** endpoint).

Match endpoint
==============

Expects:

  * object dictionary of field values for one product (must match data model provided by client)

  * num_results number of results to return (max: 10, default: 5)

  * api_key customer API key (GUID)

Example:

::

    {
      'object': { 'name': 'lettuce', 'size': '1kg' },
      'num_results': 5,
      'api_key': '929E624D-6DD7-4A2E-98AD-4A56D37A3D2A',
    }

Response:

  * object original object to match

  * matches list of objects and match confidence of size num_results that dedupe found as matches

  * api_key customer API key (GUID)

Example: 

:: 

    {
      'object': { 'name': 'letttuce', 'size': '1kg' },
      'matches': [
        { 'name': 'lettuce', 'size': '1kg', 'entity_id': 11345, 'match_confidence': 0.94 },
        { 'name': 'beans', 'size': '1kg', 'entity_id': 12245, 'match_confidence': 0.32 },
        { 'name': 'rice', 'size': '1kg', 'entity_id': 12335, 'match_confidence': 0.10 },
        { 'name': 'chicken', 'size': '1kg', 'entity_id': 12344, 'match_confidence': 0.09 },
        { 'name': 'grapes', 'size': '1kg', 'entity_id': 123455, 'match_confidence': 0.07 }
      ],
      'api_key': '929E624D-6DD7-4A2E-98AD-4A56D37A3D2A'
    }


The user will want to act based on the response of this API call in one of three ways. 

  1. **none** of the matches returned is correct - investigate and potentially add new product to canonical dataset

  2. **one** of the matches returned is correct - the product should be associated with the proper ID 

  3. **more than one** of the matches returned is correct - the canonical database is not canonical and products should be merged

Any changes to the canonical database must be made by the user. Dedupe will not have write access to the user's database.

Train endpoint
==============

Expects:

  * object original object to match

  * matches list of objects with a match flag attribute flagged by a human reviewer

  * api_key customer API key (GUID)

Example: 

:: 

    {
      'object': { 'name': 'letttuce', 'size': '1kg'},
      'matches': [
        { 'name': 'lettuce', 'size': '1kg', 'entity_id': 11345, 'match': 1 },
        { 'name': 'beans', 'size': '1kg', 'entity_id': 12245, 'match': 0 },
        { 'name': 'rice', 'size': '1kg', 'entity_id': 12335, 'match': 0 },
        { 'name': 'chicken', 'size': '1kg', 'entity_id': 12344, 'match': 0 },
        { 'name': 'grapes', 'size': '2kg', 'entity_id': 123455, 'match': 0 }
      ],
      'api_key': '929E624D-6DD7-4A2E-98AD-4A56D37A3D2A'
    }

Response:

This API call should only get zero or one positive matches. If more than one positive match is provided, it means the canonical database of products is not canonical and should be corrected on the client's side.

  * status - 200 for success or 500 for error

::

    {
      'status': 200
    }

Example python script using the match endpoint
==============================================

.. code-block:: python 

  import requests
  import json
   
  # set your session IDs
  API_KEY = 'YOUR API KEY'
  SESS_ID = 'YOUR SESSION ID'
   
  # the field names in the match_object must match the field names in your session
  match_object = {
    "name": 'john smith',
    "address": '222 W Merchandise Mart Plz, Chicago IL',
    "phone": "(555) 725-0195"
  }
   
  # post the
  post_data = {
    'api_key': API_KEY,
    'session_id': SESS_ID,
    'threshold': 0.5, # set this to a value between 0 and 1 for how conservative the returned matches should be
    'object': match_object
  }
   
  r = requests.post('https://app.dedupe.io/match/',
  data=json.dumps(post_data))
   
  # print the response from Dedupe.io
  print(r.json())

.. toctree::
    :maxdepth: 1

