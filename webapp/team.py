import random as rnd
import talisker.requests
from flask import Blueprint, render_template, request, jsonify

webteam = Blueprint(
    "webteam", __name__, template_folder="/templates", static_folder="/static"
)


api_session = talisker.requests.get_session()


def get_canonical_webmonkeys():
    response = api_session.get(
        url=(
            "https://api.launchpad.net"
            "/1.0/~canonical-webmonkeys/members_details"
        )
    )

    return response.json()


def get_member_link(url):
    response = api_session.get(url=url)

    return response.json()


def get_all_display_names():
    try:
        users = get_canonical_webmonkeys()
    except Exception:
        users = {}

    display_names = []
    if "entries" in users:
        for entry in users["entries"]:
            if "member_link" in entry:
                try:
                    user = get_member_link(entry["member_link"])
                except Exception:
                    user = {}

            if not user["is_team"]:
                if "display_name" in user:
                    # TODO Remove Chris and David from canonical-webmonkeys
                    if (
                        not user["display_name"] == "Chris Johnston"
                        and not user["display_name"] == "David Callé"
                    ):
                        display_names.append(user["display_name"])

    return display_names


@webteam.route("/")
def index():
    display_names = get_all_display_names()
    display_names.sort()

    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(display_names)
    else:
        return render_template("team/index.html", display_names=display_names)


@webteam.route("/random")
def random():
    display_names = get_all_display_names()

    context = {"user": rnd.choice(display_names)}
    return render_template("team/random.html", **context)
