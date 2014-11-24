from flask import Flask, request
from gaia.api.views import api
import os,logging
import logging.handlers

import gaia.demo.views


def create_app(config=None):
    """
    Creates the app.
    """
    # Initialize the app
    app = Flask("gaia")

    # config
    app.config.from_envvar("GAIA_SETTINGS")
    configure_blueprints(app)
    configure_logging(app)

    return app

def configure_blueprints(app):
    app.register_blueprint(api, url_prefix="/api")



def configure_logging(app):
    """
    Configures logging.
    """

    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s ')

    info_log = os.path.join(logs_folder, app.config['INFO_LOG'])


    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log,
        maxBytes=100000,
        backupCount=10
    )

    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(logs_folder, app.config['ERROR_LOG'])


    error_file_handler = logging.handlers.RotatingFileHandler(
        error_log,
        maxBytes=100000,
        backupCount=10
    )

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)




