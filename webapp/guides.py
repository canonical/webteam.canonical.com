import os
from canonicalwebteam.discourse import DiscourseAPI, DocParser, Docs
import flask

import talisker.requests

DISCOURSE_INDEX_TOPIC = 157
DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.getenv("DISCOURSE_API_USERNAME")


def init_docs(app):
    session = talisker.requests.get_session()
    discourse_docs = Docs(
        parser=DocParser(
            api=DiscourseAPI(
                base_url="https://discourse.canonical.com/",
                session=session,
                api_key=DISCOURSE_API_KEY,
                api_username=DISCOURSE_API_USERNAME,
            ),
            index_topic_id=DISCOURSE_INDEX_TOPIC,
            url_prefix="/guides",
        ),
        document_template="guides.html",
        url_prefix="/guides",
    )

    @discourse_docs.blueprint.before_request
    def before_request():
        if "openid" not in flask.session:
            return flask.redirect("/login?next=" + flask.request.path)

    discourse_docs.init_app(app)
