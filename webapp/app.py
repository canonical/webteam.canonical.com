import flask
from canonicalwebteam.flask_base.app import FlaskBase

from webapp.guides import init_docs
from webapp.sso import init_sso
from webapp.team import webteam
from webapp.releases import releases
from webapp.canonicool import canonicool
from webapp.design_assembly import design_assembly

app = FlaskBase(
    __name__,
    "webteam.canonical.com",
    template_folder="../templates",
    static_folder="../static",
)


@app.route("/")
def index():
    return flask.render_template("homepage.html")


init_sso(app)
init_docs(app)
app.register_blueprint(webteam, url_prefix="/team")
app.register_blueprint(releases, url_prefix="/releases")
app.register_blueprint(canonicool, url_prefix="/canonicool")
app.register_blueprint(design_assembly, url_prefix="/design-assembly")
