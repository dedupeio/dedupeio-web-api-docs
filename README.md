# Dedupe.io web API documentation

Documentation for Dedupe.io web API: https://apidocs.dedupe.io

Part of the [Dedupe.io](https://dedupe.io/) cloud service and open source toolset for de-duplicating and finding fuzzy matches in your data.

## Set-up 

Read the Docs suggests using Sphinx, a tool to facilitate the generation of nice-looking documentation. Before you install Sphinx, you may want to set-up a virtualized development environment: learn [how to set up virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Then, run the following in your terminal:

```bash
mkvirtualenv dedupeio-web-api-doc
git clone git@github.com:dedupeio/dedupeio-web-api-doc.git
cd dedupeio-web-api-doc
pip install -r requirements.txt
```

Afterwards, whenever you want to use this virtual environment, run `workon web-api-documentation`.

## Contribute

You can learn about the process of Sphinx and document creation on the [Read the Docs site](http://docs.readthedocs.io/en/latest/getting_started.html).

Ready to dive in? Edit the `rst` files in the `docs` directory. Then, generate the html by running the Makefile:

```bash
cd docs
make html
```

Then, view your code in a browser:

```bash
open _build/html/index.html
```

## Team

* Forest Gregg, DataMade 
* Regina Compton, DataMade 
* Derek Eder, DataMade
