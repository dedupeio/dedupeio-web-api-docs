===============================
Dedupe.io web API documentation 
===============================

Overview
========
Dedupe.io is a a software as a service platform for quickly and accurately identifying clusters of similar records across one or more files or databases. 

When to use the web API
=======================
Once you have completed the de-duping process for a project, you can continue to incrementally check, match and add to it via API calls. 
 
By posting a chunk of data to the API (described in the **match** endpoint), Dedupe.io can compare it to your dataset and return one or more potential matches. In the case where more than one result is returned, you can optionally tell Dedupe.io which one is correct and it will update the training for your dataset based on it (described in the **train** endpoint).

API access
==========

API access is available for Dedupe.io Subscription accounts. For more information, see our `pricing page <https://dedupe.io/pricing/>`_.

Your API key can be found on the `My Account page <https://app.dedupe.io/my-account/>`_.

Your Project ID and example API calls can be found on the Settings page for your project.

All methods are accessed via: **https://app.dedupe.io/api/v1/ENDPOINT**

.. toctree::
    :maxdepth: 1

    Endpoints
    Examples