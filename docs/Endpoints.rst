Sending records to match
========================

.. http:post:: /match

   Send one record to check for matches against a Dedupe.io project

   :query api_key: user API key
   :query project_id: identifier for project to match against
   :query object: dictionary of field values for one product (must match data model provided by client)
   :query num_results: number of results to return (default: 5)
   :query threshold: minimum matching confidence score of results returned

   **Example request**:

   .. sourcecode:: http

      POST /match HTTP/1.1
      Host: dedupe.io
      Accept: application/json, text/javascript

      {
        'api_key': '50b400ed-cc7f-4bbb-b16f-13dbdc022e91',
        'project_id': 'ebfc2317-7050-4e89-992c-56bcab13f1a1',
        'object': { 'name': 'lettuce', 'size': '1kg' },
        'num_results': 3,
        'threshold': 0.8,
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
        'object': { 'name': 'letttuce', 'size': '1kg' },
        'matches': [
          { 'name': 'lettuce', 'size': '1kg', 'entity_id': 11345, 'match_confidence': 0.94 },
          { 'name': 'beans', 'size': '1kg', 'entity_id': 12245, 'match_confidence': 0.32 },
          { 'name': 'rice', 'size': '1kg', 'entity_id': 12335, 'match_confidence': 0.10 },
          { 'name': 'chicken', 'size': '1kg', 'entity_id': 12344, 'match_confidence': 0.09 },
          { 'name': 'grapes', 'size': '1kg', 'entity_id': 123455, 'match_confidence': 0.07 }
        ],
        'api_key': '50b400ed-cc7f-4bbb-b16f-13dbdc022e91'
      }


The user will want to act based on the response of this API call in one of three ways. 

  1. **none** of the matches returned is correct - investigate and potentially add new product to canonical dataset

  2. **one** of the matches returned is correct - the product should be associated with the proper ID 

  3. **more than one** of the matches returned is correct - the canonical database is not canonical and products should be merged

Any changes to the canonical database must be made by the user. Dedupe will not have write access to the user's database.

Providing training from matches
===============================

.. http:post:: /train

   Send a tagged record to a Dedupe.io project for training. 

   This API call should only get zero or one positive matches. If more than one positive match is provided, it means the canonical database of products is not canonical and should be corrected on the client's side.

   :query api_key: customer API key
   :query project_id: identifier for project to train
   :query object: original object to match
   :query matches: list of objects with a match flag attribute flagged by a human reviewer
   
   **Example request**:

   .. sourcecode:: http

      POST /train HTTP/1.1
      Host: dedupe.io
      Accept: application/json, text/javascript

      {
        'object': { 'name': 'letttuce', 'size': '1kg'},
        'matches': [
          { 'name': 'lettuce', 'size': '1kg', 'entity_id': 11345, 'match': 1 },
          { 'name': 'beans', 'size': '1kg', 'entity_id': 12245, 'match': 0 },
          { 'name': 'rice', 'size': '1kg', 'entity_id': 12335, 'match': 0 },
          { 'name': 'chicken', 'size': '1kg', 'entity_id': 12344, 'match': 0 },
          { 'name': 'grapes', 'size': '2kg', 'entity_id': 123455, 'match': 0 }
        ],
        'api_key': '50b400ed-cc7f-4bbb-b16f-13dbdc022e91'
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript