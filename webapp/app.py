import flask
from canonicalwebteam.flask_base.app import FlaskBase

from webapp.guides import discourse_docs
from webapp.team import webteam
from webapp.releases import releases
from webapp.canonicool import canonicool

app = FlaskBase(
    __name__,
    "webteam.canonical.com",
    template_folder="../templates",
    static_folder="../static",
)


@app.route("/")
def index():
    return flask.render_template("homepage.html")


app.register_blueprint(webteam, url_prefix="/team")
app.register_blueprint(releases, url_prefix="/releases")
app.register_blueprint(canonicool, url_prefix="/canonicool")
discourse_docs.init_app(app)
