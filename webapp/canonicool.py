from flask import Blueprint

canonicool = Blueprint(
    "canonicool",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


@canonicool.route("/")
def index():
    return "Hello"
