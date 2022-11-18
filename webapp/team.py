import random as rnd
from launchpadlib.launchpad import Launchpad
from flask import Blueprint, render_template, request, jsonify

webteam = Blueprint(
    "webteam", __name__, template_folder="/templates", static_folder="/static"
)


def get_all_display_names():
    lp = Launchpad.login_anonymously(
        "webteam.canonical.com", "production", ".", version="devel"
    )
    team = lp.people["canonical-webmonkeys"]

    return [person.display_name for person in team.members]


def get_all_teams():
    return [
        "User research",
        "Sites",
        "Workplace Engineering",
        "MAAS",
        "Marketplaces",
        "Design system",
        "Commercial",
        "Landscape",
        "Kernel factory",
        "LXD Anbox",
        "Systems",
    ]


def get_all_mattermost_handles():
    lp = Launchpad.login_anonymously(
        "webteam.canonical.com", "production", ".", version="devel"
    )
    team = lp.people["canonical-webmonkeys"]

    return [person.name for person in team.members]


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
    team_names = get_all_teams()

    context = {
        "user": rnd.choice(display_names),
        "teams": rnd.sample(team_names, len(team_names)),
    }

    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(context)
    else:
        return render_template("team/random.html", **context)


@webteam.route("/mattermost")
def mattermost():
    mattermost_handles = get_all_mattermost_handles()
    mattermost_handles.sort()

    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(mattermost_handles)
    else:
        return render_template(
            "team/mattermost.html", mattermost_handles=mattermost_handles
        )


@webteam.after_request
def add_headers(response):
    if response.status_code == 200:
        response.headers["Cache-Control"] = "private"

    return response
