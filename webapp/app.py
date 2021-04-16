# Core
import datetime
import json
import re
import os

# Packages
import flask
import requests
import humanize

app = flask.Flask(__name__, template_folder="../templates")

domain_repositories = [
    {
        "production_domain": "360.canonical.com",
        "staging_domain": "360.staging.canonical.com",
        "repository": "canonical-web-and-design/360.canonical.com",
    },
    {
        "production_domain": "anbox-cloud.io",
        "staging_domain": "staging.anbox-cloud.io",
        "repository": "canonical-web-and-design/anbox-cloud.io",
    },
    {
        "production_domain": "certification.ubuntu.com",
        "staging_domain": "certification.staging.ubuntu.com",
        "repository": "canonical-web-and-design/certification.ubuntu.com",
    },
    {
        "production_domain": "charmed-osm.com",
        "staging_domain": "staging.charmed-osm.com",
        "repository": "canonical-web-and-design/charmed-osm.com",
    },
    {
        "production_domain": "cloud-init.io",
        "staging_domain": "staging.cloud-init.io",
        "repository": "canonical-web-and-design/cloud-init.io",
    },
    {
        "production_domain": "cn.ubuntu.com",
        "staging_domain": "cn.staging.ubuntu.com",
        "repository": "canonical-web-and-design/cn.ubuntu.com",
    },
    {
        "production_domain": "design.ubuntu.com",
        "staging_domain": "design.staging.ubuntu.com",
        "repository": "canonical-web-and-design/design.ubuntu.com",
    },
    {
        "production_domain": "docs.conjure-up.io",
        "staging_domain": "docs.staging.conjure-up.io",
        "repository": "canonical-web-and-design/docs.conjure-up.io",
    },
    {
        "production_domain": "docs.ubuntu.com",
        "staging_domain": "docs.staging.ubuntu.com",
        "repository": "canonical-web-and-design/docs.ubuntu.com",
    },
    {
        "production_domain": "jaas.ai",
        "staging_domain": "staging.jaas.ai",
        "repository": "canonical-web-and-design/jaas.ai",
    },
    {
        "production_domain": "jp.ubuntu.com",
        "staging_domain": "jp.staging.ubuntu.com",
        "repository": "canonical-web-and-design/jp.ubuntu.com",
    },
    {
        "production_domain": "limenet.snapcraft.io",
        "staging_domain": "limenet.staging.snapcraft.io",
        "repository": "canonical-web-and-design/snapcraft.io",
    },
    {
        "production_domain": "maas.io",
        "staging_domain": "staging.maas.io",
        "description": "Not automatically updated",
        "repository": "canonical-web-and-design/maas.io",
    },
    {
        "production_domain": "manager.assets.ubuntu.com",
        "staging_domain": "manager.assets.staging.ubuntu.com",
        "repository": "canonical-web-and-design/manager.assets.ubuntu.com",
    },
    {
        "production_domain": "microk8s.io",
        "staging_domain": "staging.microk8s.io",
        "repository": "canonical-web-and-design/microk8s.io",
    },
    {
        "production_domain": "microstack.run",
        "staging_domain": "staging.microstack.run",
        "repository": "canonical-web-and-design/microstack.run",
    },
    {
        "production_domain": "mir-server.io",
        "staging_domain": "staging.mir-server.io",
        "repository": "canonical-web-and-design/mir-server.io",
    },
    {
        "production_domain": "multipass.run",
        "staging_domain": "staging.multipass.run",
        "repository": "canonical-web-and-design/multipass.run",
    },
    {
        "production_domain": "netplan.io",
        "staging_domain": "staging.netplan.io",
        "repository": "canonical-web-and-design/netplan.io",
    },
    {
        "production_domain": "old-docs.jujucharms.com",
        "staging_domain": "old-docs.staging.jujucharms.com",
        "repository": "juju/docs",
    },
    {
        "production_domain": "snapcraft.io",
        "staging_domain": "staging.snapcraft.io",
        "repository": "canonical-web-and-design/snapcraft.io",
    },
    {
        "production_domain": "sdrsatcom.snapcraft.io",
        "staging_domain": "sdrsatcom.staging.snapcraft.io",
        "description": "Not automatically updated",
        "repository": "canonical-web-and-design/snapcraft.io",
    },
    {
        "production_domain": "ubuntu.com",
        "staging_domain": "staging.ubuntu.com",
        "repository": "canonical-web-and-design/ubuntu.com",
    },
    {
        "production_domain": "vanillaframework.io",
        "staging_domain": "staging.vanillaframework.io",
        "repository": "canonical-web-and-design/vanilla-framework",
    },
]


@app.route("/")
def index():
    return flask.render_template(
        "index.html", domain_repositories=domain_repositories
    )


@app.route("/domain-info.json")
def domain_info():
    production_domain = flask.request.args["domain"]
    staging_domain_parts = production_domain.split(".")
    staging_domain_parts.insert(-2, "staging")
    staging_domain = ".".join(staging_domain_parts)
    repository = flask.request.args["repo"]

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
                        "for %s" % (staging_domain)
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
                        " for %s" % (production_domain)
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
                        " for %s in unexpected format" % (staging_domain)
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
                        " for %s in unexpected format" % (production_domain)
                    }
                ),
                402,
                {"Content-Type": "application/json"},
            )
    else:
        headers = {
            "authorization": f"Bearer {os.getenv('RELEASES_GITHUB_TOKEN')}",
            "Accept": "application/vnd.github.groot-preview+json",
        }

        response = requests.get(
            f"https://api.github.com/repos/{repository}/commits/"
            f"{staging_match.group(2)}/pulls",
            headers=headers,
        )
        pr_title = ""
        pr_author = ""
        pr_url = ""
        pr_author_url = ""

        if response.status_code == 200:
            pr_data = response.json()
            pr_title = pr_data[0]["title"]
            pr_url = pr_data[0]["html_url"]
            pr_author = pr_data[0]["user"]["login"]
            pr_author_url = pr_data[0]["user"]["html_url"]

    staging = {
        "domain": staging_domain,
        "imageTag": staging_image_tag,
        "epochTime": int(staging_match.group(1)),
        "commitId": staging_match.group(2),
        "humanTime": humanize.naturaltime(
            datetime.datetime.fromtimestamp(int(staging_match.group(1)))
        ),
        "prTitle": pr_title,
        "prUrl": pr_url,
        "prAuthor": pr_author,
        "prAuthorUrl": pr_author_url,
    }

    production = {
        "domain": production_domain,
        "imageTag": production_image_tag,
        "epochTime": int(production_match.group(1)),
        "commitId": production_match.group(2),
        "humanTime": datetime.datetime.fromtimestamp(
            int(production_match.group(1))
        ).strftime("%c %Z"),
    }

    return (
        json.dumps({"staging": staging, "production": production}),
        200,
        {"Content-Type": "application/json"},
    )
