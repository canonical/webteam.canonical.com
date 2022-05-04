import flask
from canonicalwebteam.flask_base.app import FlaskBase

from webapp.canonicool import canonicool
from webapp.masterclasses import masterclasses
from webapp.design_assembly import design_assembly
from webapp.guides import bootstrap_guides
from webapp.practices import bootstrap_practices
from webapp.releases import releases
from webapp.sso import init_sso
from webapp.team import webteam

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
app.register_blueprint(masterclasses, url_prefix="/masterclasses")
app.register_blueprint(design_assembly, url_prefix="/design-assembly")
bootstrap_guides(app)
bootstrap_practices(app)
init_sso(app)
