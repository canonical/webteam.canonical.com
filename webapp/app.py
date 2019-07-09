# Core
import datetime
import json
import re

# Packages
import flask
import requests

app = flask.Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/domain-info.json")
def domain_info():
    production_domain = flask.request.args["domain"]
    staging_domain_parts = production_domain.split(".")
    staging_domain_parts.insert(-2, "staging")
    staging_domain = ".".join(staging_domain_parts)

    staging_response = requests.get(f"https://{staging_domain}/_status/check")
    response = requests.get(f"https://{production_domain}/_status/check")

    staging_image_tag = staging_response.headers.get("x-vcs-revision")
    production_image_tag = response.headers.get("x-vcs-revision")

    if not staging_image_tag or not production_image_tag:
        if not staging_image_tag:
            return (
                json.dumps(
                    {
                        "error": f"Couldn't find image tag "
                        "for {staging_domain}"
                    }
                ),
                402,
                {"Content-Type": "application/json"},
            )
        else:
            return (
                json.dumps(
                    {
                        "error": f"Couldn't find image tag"
                        " for {production_domain}"
                    }
                ),
                402,
                {"Content-Type": "application/json"},
            )

    staging_match = re.match(r"(\d{10})-([\da-f]{7})", staging_image_tag)
    production_match = re.match(r"(\d{10})-([\da-f]{7})", production_image_tag)

    if not staging_match or not production_match:
        if not staging_match:
            return (
                json.dumps(
                    {
                        "error": f"Image tag '{staging_image_tag}'"
                        " for {staging_domain} in unexpected format"
                    }
                ),
                402,
                {"Content-Type": "application/json"},
            )
        else:
            return (
                json.dumps(
                    {
                        "error": f"Image tag '{production_image_tag}'"
                        " for {production_domain} in unexpected format"
                    }
                ),
                402,
                {"Content-Type": "application/json"},
            )
    staging = {
        "domain": staging_domain,
        "imageTag": staging_image_tag,
        "epochTime": int(staging_match.group(1)),
        "commitId": staging_match.group(2),
        "humanTime": datetime.datetime.fromtimestamp(
            int(staging_match.group(1))).strftime("%c %Z")
    }

    production = {
        "domain": production_domain,
        "imageTag": production_image_tag,
        "epochTime": int(production_match.group(1)),
        "commitId": production_match.group(2),
        "humanTime": datetime.datetime.fromtimestamp(
            int(production_match.group(1))).strftime("%c %Z")
    }

    return (
        json.dumps(
            {
                "staging": staging,
                "production": production,
            }
        ),
        200,
        {"Content-Type": "application/json"},
    )
