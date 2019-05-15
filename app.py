# Core
import datetime
import json
import re

# Packages
import flask
import requests

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/domain-info.json")
def domain_info():
    domain = flask.request.args["domain"]
    staging_domain_parts = domain.split(".")
    staging_domain_parts.insert(-2, "staging")
    staging_domain = ".".join(staging_domain_parts)

    response = requests.get(f"https://{staging_domain}/_status/check")

    image_tag = response.headers.get("x-vcs-revision")

    if not image_tag:
        return (
            json.dumps(
                {"error": f"Couldn't find image tag for {staging_domain}"}
            ),
            402,
            {"Content-Type": "application/json"},
        )

    match = re.match(r"(\d{10})-([\da-f]{7})", image_tag)

    if not match:
        return (
            json.dumps(
                {
                    "error": f"Image tag '{image_tag}' for {staging_domain}"
                    " in unexpected format"
                }
            ),
            402,
            {"Content-Type": "application/json"},
        )

    epoch_time = int(match.group(1))
    commit_id = match.group(2)

    human_time = datetime.datetime.fromtimestamp(epoch_time).strftime("%c %Z")

    return (
        json.dumps(
            {
                "domain": domain,
                "stagingDomain": staging_domain,
                "imageTag": image_tag,
                "epochTime": epoch_time,
                "humanTime": human_time,
                "commitId": commit_id,
            }
        ),
        200,
        {"Content-Type": "application/json"},
    )
