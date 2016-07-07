# Multiple DocuSign Signature REST API recipes in Python

Repo: esignature-recipes-python

This repo contains a Python Flask application that demonstrates several of the 
DocuSign Signature REST API recipes:

* Embedded signing. See app/py_001_embedded_signing
* Sending a signature request via email. See app/py_004_email_send
* Sending a signature request using a template. See app/py_002_email_send_template
* Using a webhook to receive status changes. See app/lib_master_python/ds_webhook.py
* Authenticating with the Signature REST API. See app/lib_master_python/ds_authentication.py

## Try it on Heroku
Use the deploy button to immediatelty try this app on Heroku. You can use Heroku’s free service tier, no credit card is needed.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Note: during the Heroku *build* process, the setup.py step for **lxml** takes several minutes since it includes a compilation.

## Run the app locally

1. Install a recent version of Python 2.x, eg 2.7.11 or later.
1. Install pip
1. Clone this repo to your computer
1. `cd` to the repo’s directory
1. `pip install -r requirements.txt` # installs the application’s requirements
1. `python run.py` # starts the application on port 5000
1. Use a browser to load [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Have a question? Pull request?
If you have a question about the Signature REST API, please use StackOverflow and tag your question with `docusignapi`

For bug reports and pull requests, please use this repo’s issues page.
