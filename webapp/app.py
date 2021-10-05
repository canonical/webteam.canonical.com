import flask
from canonicalwebteam.flask_base.app import FlaskBase

from webapp.guides import discourse_docs
from webapp.team import webteam
from webapp.releases import releases
from webapp.eight_ball import eight_ball

app = FlaskBase(
    __name__,
    "webteam.canonical.com",
    template_folder="../templates",
    static_folder="../static",
)


@app.route("/")
@app.route("/create")
def index():
    return flask.render_template("homepage.html")


app.register_blueprint(webteam, url_prefix="/team")
app.register_blueprint(releases, url_prefix="/releases")
app.register_blueprint(eight_ball, url_prefix="/eight-ball")
discourse_docs.init_app(app)


# Path for all the static files (compiled JS/CSS, etc.) for the 
# 8-ball app. This should be in the blueprint, but then it does
# not work
@app.route("/<path:path>")
def home(path):
    return flask.send_from_directory("../eight-ball/public", path)