from flask import render_template, flash, redirect, jsonify
from app import app
from app.lib_master_python import ds_recipe_lib
from app.lib_master_python import ds_authentication
from app.lib_master_python import ds_webhook
from app.lib_master_python import ds_api_logging
import httplib

@app.route('/')
def index():
    return render_template('home.html', title='Home - Python Recipes', base_url=ds_recipe_lib.get_base_url(0))

@app.route('/index')
def r_index():
    redirect("/")

################################################################################
################################################################################

# Authentication
@app.route('/auth', methods=['GET'])
def get_auth_status():
    return jsonify(ds_authentication.get_auth_status())

@app.route('/auth', methods=['POST'])
def set_auth():
    return jsonify(ds_authentication.set_auth())

@app.route('/auth', methods=['DELETE'])
def delete_auth():
    return jsonify(ds_authentication.delete_auth())

@app.route('/auth_redirect', methods=['GET'])
def auth_redirect():
    err = ds_authentication.auth_redirect()
    # err is False or an error message
    # We will use the Flash technique to show the message on the home page.
    # Or a simpler alternative would be to show the error message on an intermediate
    # page, with a "Continue" link to the home page
    if err:
        flash(err)
    return redirect("/")

@app.route('/auth_token', methods=['DELETE'])
def auth_token_delete():
    r = ds_authentication.auth_token_delete()
    # r[err] is False or an error message
    # Deletes the authentication token on DocuSign
    return jsonify(r)

################################################################################
################################################################################

# Webhook
@app.route('/webhook_status', methods=['GET'])
def get_webhook_status():
    return jsonify(ds_webhook.get_webhook_status())

@app.route('/webhook_status', methods=['POST'])
def set_webhook_status():
    return jsonify(ds_webhook.set_webhook_status())

@app.route('/webhook', methods=['POST']) # The listener called by DocuSign
def webhook():
    ds_webhook.webhook_listener()
    return ("", httplib.NO_CONTENT) # no content

@app.route('/webhook_status_page/<envelope_id>') # initial status page
def webhook_status_page(envelope_id):
    r = ds_webhook.status_page(envelope_id)
    return render_template('webhook_status_page.html', title='Notifications - Webhook--Python', data=r, base_url=ds_recipe_lib.get_base_url(2))

@app.route('/webhook_status_items/<envelope_id>') # list all status items
def webhook_status_items(envelope_id):
    r = ds_webhook.status_items(envelope_id)
    return jsonify(items=r)

################################################################################
################################################################################

# API Logging
@app.route('/logging_page', methods=['GET'])
def logging_page():
    return render_template('log_status_page.html', title='API Logging', base_url=ds_recipe_lib.get_base_url(2))

@app.route('/logs_download', methods=['POST'])
def logs_download():
    return jsonify(ds_api_logging.logs_download())

@app.route('/logging_status', methods=['GET'])
def get_logging_status():
    return jsonify(ds_api_logging.get_logging_status())

@app.route('/logs_list', methods=['GET'])
def logs_list():
    return jsonify(ds_api_logging.logs_list())


################################################################################
################################################################################

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

