import random as rnd
from typing import Any, List, TypedDict

from flask import Blueprint, jsonify, render_template, request
from launchpadlib.launchpad import Launchpad

from webapp.utils import lru_cache


class TeamMember(TypedDict):
    name: str
    username: str


webteam = Blueprint(
    "webteam", __name__, template_folder="/templates", static_folder="/static"
)


def lp_instance():
    return Launchpad.login_anonymously(
        "webteam.canonical.com", "production", ".", version="devel"
    )


def map_person(person: Any) -> TeamMember:
    return {
        "name": person.display_name,
        "username": person.name,
    }


@lru_cache(ttl_seconds=60 * 10)
def get_team_members(team_name: str) -> List[TeamMember]:
    lp = lp_instance()
    team = lp.people[team_name]
    members = [map_person(person) for person in team.members]
    members.sort(key=lambda x: x["name"])
    return members


def exclude_team_members(
    team: List[TeamMember], exclude: List[str]
) -> List[TeamMember]:
    exclude_set = set([member["username"] for member in exclude])
    all_set = set([member["username"] for member in team])
    map_username = {member["username"]: member for member in team}
    return [map_username[username] for username in all_set - exclude_set]


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
        "Desktop",
    ]


@webteam.route("/")
def index():
    all_members_names = [
        member["name"] for member in get_team_members("canonical-webmonkeys")
    ]
    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(all_members_names)
    else:
        return render_template(
            "team/index.html", display_names=all_members_names
        )


@webteam.route("/mattermost")
def mattermost():
    mattermost_handles = [
        person["username"]
        for person in get_team_members("canonical-webmonkeys")
    ]

    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(mattermost_handles)
    else:
        return render_template(
            "team/mattermost.html", mattermost_handles=mattermost_handles
        )


@webteam.route("/random")
def random():
    all_members = get_team_members("canonical-webmonkeys")
    engineers = get_team_members("canonical-web-engineers")
    designers = exclude_team_members(all_members, engineers)
    team_names = get_all_teams()

    context = {
        "member": rnd.choice(all_members),
        "engineer_member": rnd.choice(engineers),
        "designer_member": rnd.choice(designers),
        "teams": rnd.sample(team_names, len(team_names)),
    }

    if request.headers.get(
        "Content-Type"
    ) and "application/json" in request.headers.get("Content-Type"):
        return jsonify(context)
    else:
        return render_template("team/random.html", **context)


@webteam.after_request
def add_headers(response):
    if response.status_code == 200:
        response.headers["Cache-Control"] = "private"

    return response
