from flask import Blueprint, send_from_directory

eight_ball = Blueprint(
    "eight_ball",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


# Path for our main Svelte page
@eight_ball.route("/")
@eight_ball.route("/<path:path>")
def app():
    if path:
        return send_from_directory("../eight-ball/public", path)
    else:
        return send_from_directory("../eight-ball/public", "index.html")


# Path for all the static files (compiled JS/CSS, etc.)
@eight_ball.route("/<path:path>")
def home(path):
    return send_from_directory("../eight-ball/public", path)
