from flask import Flask, request
from gaia.api.views import api
import gaia.demo.views 



def create_app(config=None):
    """
    Creates the app.
    """
    # Initialize the app
    app = Flask("gaia")

    # config
    app.config.from_envvar("GAIA_SETTINGS")


    #configure_extensions(app)
    configure_blueprints(app)
    #configure_logging(app)
    #configure_jinja2(app)

    return app

def configure_blueprints(app):
    app.register_blueprint(api, url_prefix="/api")





