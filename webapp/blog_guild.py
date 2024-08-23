from datetime import datetime

import flask

from webapp.spreadsheet import MissingCredential, get_sheet

SPREADSHEET_ID = "1MhVXVE2cwR_rZ0TLyk5-wv2KKFRY72z3bPRf7r0qY_8"

blog_guild = flask.Blueprint(
    "blog-guild",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


def get_value_row(row, type):
    if row:
        if type == datetime:
            if "formattedValue" in row:
                return {
                    "Formatted": datetime.strptime(
                        row["formattedValue"], "%d %B %Y"
                    ).strftime("%d %b %Y"),
                    "Object": datetime.strptime(
                        row["formattedValue"], "%d %B %Y"
                    ),
                }
        elif "userEnteredValue" in row:
            if "stringValue" in row["userEnteredValue"]:
                if (
                    "userEnteredFormat" in row
                    and "textFormat" in row["userEnteredFormat"]
                    and "link" in row["userEnteredFormat"]["textFormat"]
                ):
                    return row["userEnteredFormat"]["textFormat"]["link"][
                        "uri"
                    ]  # noqa
                return type(row["userEnteredValue"]["stringValue"])
            if "numberValue" in row["userEnteredValue"]:
                return type(row["userEnteredValue"]["numberValue"])

    return ""


def index_in_list(a_list, index):
    return index < len(a_list)


# Parse the id from a google url
# https://drive.google.com/open?id=15cy6HFRkzgidDQ1Ff1wBDP-TVihfg_15
# https://drive.google.com/file/d/1YkOAdSwmAHmddwhQ2l0sbEQyflbkhQ5L/view
# https://drive.google.com/file/d/1nCbTZtX380e6lD1kkQ6BjTA0aAknZJGY/view?usp=drivesdk
# https://drive.google.com/file/d/1TQLA53RPhf20Q9BeqMN6e1DFb_kPsF91/view?usp=drive_web
def get_id(video_link):
    if video_link:
        if "id=" in video_link:
            return video_link.split("id=")[1]
        elif "file/d/" in video_link:
            return video_link.split("file/d/")[1].split("/view")[0]
    return ""


@blog_guild.route("/")
def index():
    blogs = get_blogs()

    return flask.render_template(
        "blog-guild.html",
        blogs=blogs,
    )


def get_blogs():
    try:
        sheet = get_sheet()
    except MissingCredential as error:
        flask.abort(500, str(error))

    SHEET = "Blogs"
    RANGE = "A2:E1000"
    COLUMNS = [
        ("Owner", str),
        ("URL", str),
        ("RSS", str),
        ("Level", str),
        ("Goals", str),
    ]
    res = sheet.get(
        spreadsheetId=SPREADSHEET_ID,
        ranges=[f"{SHEET}!{RANGE}"],
        includeGridData=True,
    ).execute()

    blogs = []
    for row in res["sheets"][0]["data"][0]["rowData"]:
        if "values" in row and row["values"][0]:
            blog = {}
            for column_index in range(len(COLUMNS)):
                (column, type) = COLUMNS[column_index]
                blog[column] = get_value_row(
                    (
                        row["values"][column_index]
                        if index_in_list(row["values"], column_index)
                        else None
                    ),
                    type,
                )

            blogs.append(blog)

    return blogs
