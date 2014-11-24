from flask import Blueprint, flash, request, redirect, url_for
from gaia.api.core import api_manager
import json

api = Blueprint("api", __name__)

@api.route("/",methods=["GET","POST"])
def call():
    method = request.form.get('method')
    params = request.form.get('params')
    response = api_manager.dispatch(method, json.loads(params))
    return response

