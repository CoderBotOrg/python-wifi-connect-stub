#!/usr/bin/python

import os
import logging
import logging.handlers
import connexion

from flask_cors import CORS

# Logging configuration
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))

## (Connexion) Flask app configuration

# Serve a custom version of the swagger ui (Jinja2 templates) based on the default one
#  from the folder 'swagger-ui'. Clone the 'swagger-ui' repository inside the backend folder
options = {"swagger_ui": False}
connexionApp = connexion.App(__name__, options=options)

# Connexion wraps FlaskApp, so app becomes connexionApp.app
app = connexionApp.app
# Access-Control-Allow-Origin
CORS(app)
app.debug = False

## New API and web application

# API v1 is defined in v1.yml and its methods are in api.py
connexionApp.add_api('v1.yml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True, use_reloader=False, threaded=True)
