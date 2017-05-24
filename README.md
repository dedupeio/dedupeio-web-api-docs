# web-api-documentation

Documentation for Dedupe Web API. Available on [readthedocs.io](http://dedupe-web-api.readthedocs.io/en/latest/).

## Set-up 

Read the Docs suggests using Sphinx, a tool to facilitate the generation of nice-looking documentation. Before you install Sphinx, you may want to set-up a virtualized development environment: learn [how to set up virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Then, run the following in your terminal:

```bash
mkvirtualenv web-api-documentation
git clone git@github.com:dedupeio/web-api-documentation.git
cd web-api-documentation
pip install -r requirements.txt
```

Afterwards, whenever you want to use this virtual environment, run `workon web-api-documentation`.

## Contribute

You can learn about the process of Sphinx and document creation on the [Read the Docs site](http://docs.readthedocs.io/en/latest/getting_started.html).

Ready to dive in? Edit the `rst` files in the `docs` directory. Then, generate the html, and view your results: you can do this by running the Makefile.

```bash
cd docs
make html
```

## Team

* Forest Gregg, DataMade 
* Regina Compton, DataMade 
