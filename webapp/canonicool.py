import requests
import os

from datetime import datetime
from dateutil import parser
from flask import Blueprint, render_template

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

    future_events = []
    past_events = []

    today = datetime.today()

    for canonicool_session in response.json():
        session_date = parser.parse(canonicool_session["date"])
        if today > session_date.replace(tzinfo=None):
            past_events.append(canonicool_session)
        elif today <= session_date.replace(tzinfo=None):
            future_events.append(canonicool_session)

    return render_template(
        "canonicool.html", past_events=past_events, future_events=future_events
    )
