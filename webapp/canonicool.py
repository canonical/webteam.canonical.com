import requests
import os
import humanize

from datetime import datetime
from dateutil import parser
from flask import Blueprint, render_template, request

DEPLOYMENT_ID = os.getenv(
    "DEPLOYMENT_ID",
    "AKfycbwM5X59etlXHY8zfl-TnHIHF9B6Wi_-w0dq4Q1OhirunKpitzhAAezKtJAGeUYsHaXz",
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
    limit = request.args.get("limit", default=6, type=int)
    offset = request.args.get("offset", default=0, type=int)
    page = request.args.get('page', default=1, type=int)
    response = requests.get(CANONICOOL_SHEET_URL)

    future_events = []
    past_events = []

    today = datetime.today()

    for canonicool_session in response.json():
        session_date = parser.parse(canonicool_session["date"])
        canonicool_session["human_date"] = humanize.naturalday(session_date)
        if today > session_date.replace(tzinfo=None):
            past_events.insert(0, canonicool_session)
        elif today <= session_date.replace(tzinfo=None):
            future_events.append(canonicool_session)

    return render_template(
        "canonicool.html", past_events=past_events, future_events=future_events, page=page, limit=limit, offset=offset
    )
