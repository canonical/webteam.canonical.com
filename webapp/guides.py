import talisker.requests

from canonicalwebteam.discourse import DiscourseAPI, DocParser, Docs

discourse_index_id = 14129

session = talisker.requests.get_session()
discourse_docs = Docs(
    parser=DocParser(
        api=DiscourseAPI(
            base_url="https://discourse.ubuntu.com/", session=session
        ),
        index_topic_id=discourse_index_id,
        url_prefix="/guides",
    ),
    document_template="guides.html",
    url_prefix="/guides",
)
