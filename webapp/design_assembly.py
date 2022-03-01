import requests
import os
import hashlib

from datetime import datetime, timedelta
from dateutil import parser
from flask import Blueprint, render_template, request

DEPLOYMENT_ID = os.getenv(
    "DEPLOYMENT_ID",
    "AKfycbyMHB6E0ErhpuO2Om1UsZ6gveh3oADt0gjp_IJoFUqoEUYCtS0sJ4mRnlfYNQ26ynG4PA",
)
DESIGN_ASSEMBLY_SHEET_URL = (
    f"https://script.google.com/macros/s/{DEPLOYMENT_ID}/exec"
)

design_assembly = Blueprint(
    "design_assembly",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


def hash_email(email):
    return hashlib.md5(email.encode("utf-8")).hexdigest()


@design_assembly.route("/")
def index():
    page = request.args.get("page", default=1, type=int)
    response = requests.get(DESIGN_ASSEMBLY_SHEET_URL)

    future_events = []
    past_events = []

    today = datetime.today().date()

    for event in response.json():
        hour = timedelta(hours=1)
        # for some reason the date is coming through as 11pm the previous day
        # of the date given in the spreadsheet, so we add an hour to get the
        # correct date
        corrected_datetime = parser.parse(event["date"]) + hour
        event_date = corrected_datetime.date()
        event["human_date"] = event_date.strftime("%d/%m/%Y")

        if today > event_date:
            past_events.insert(0, event)
        elif today <= event_date:
            future_events.append(event)

    events_per_page = 3
    return render_template(
        "design-assembly.html",
        past_events=past_events,
        future_events=future_events,
        page=page,
        total_pages=len(past_events) / events_per_page,
        events_per_page=events_per_page,
    )
