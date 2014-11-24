from flask import Blueprint, flash, request, redirect, url_for
from gaia.api.core import api_manager
import json
import time
from flask import current_app
api = Blueprint("api", __name__)

@api.route("/",methods=["GET","POST"])
def call():
    start = time.time()
    method = request.form.get('method')
    params = request.form.get('params')
    rpcdata = api_manager.dispatch(method, json.loads(params))
    data = {}
    data["result"] = rpcdata
    end = time.time()
    cost = end - start
    current_app.logger.info("%s %f",method,cost)
    return json.dumps(data)

