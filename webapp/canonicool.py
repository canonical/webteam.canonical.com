import requests
import os
from flask import Blueprint, jsonify

DEPLOYMENT_ID = os.getenv(
    "DEPLOYMENT_ID",
    "AKfycbwahRHxgFZQSDCYn-jiSKf8ihsX1yBpdLtFOjTvADMp3fRpJ4dCuVU1OxX_rn4793ZY",
)
CANONICOOL_SHEET_URL = (
    f"https://script.google.com/macros/s/{DEPLOYMENT_ID}/exec"
)

canonicool = Blueprint(
    "canonicool",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


@canonicool.route("/")
def index():
    response = requests.get(CANONICOOL_SHEET_URL)

    return jsonify(response.json())
