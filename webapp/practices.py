import os
from canonicalwebteam.discourse import DiscourseAPI, DocParser, Docs

import talisker.requests

DISCOURSE_INDEX_TOPIC = 260
DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.getenv("DISCOURSE_API_USERNAME")


def bootstrap_practices(app):
    session = talisker.requests.get_session()
    practices = Docs(
        blueprint_name="practices",
        parser=DocParser(
            api=DiscourseAPI(
                base_url="https://discourse.canonical.com/",
                session=session,
                api_key=DISCOURSE_API_KEY,
                api_username=DISCOURSE_API_USERNAME,
            ),
            index_topic_id=DISCOURSE_INDEX_TOPIC,
            url_prefix="/practices",
        ),
        document_template="docs.html",
        url_prefix="/practices",
    )

    practices.init_app(app)
