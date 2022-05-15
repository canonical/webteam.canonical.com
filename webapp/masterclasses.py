from datetime import datetime
from flask import Blueprint, render_template
from webapp.spreadsheet import get_sheet


SPREADSHEET_ID = "1fFumFWIM3oHwLr9pcBlaANcadAU0bNJxbkfGKwC_1pg"
sheet = get_sheet()

masterclasses = Blueprint(
    "masterclasses",
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
                if "link" in row["userEnteredFormat"]["textFormat"]:
                    return row["userEnteredFormat"]["textFormat"]["link"][
                        "uri"
                    ]
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


@masterclasses.route("/")
def index():
    if sheet is None:
        return render_template("masterclasses.html", sessions=[])

    SHEET = "Completed"
    RANGE = "A2:G1000"
    COLUMNS = [
        ("Topic", str),
        ("Owner", str),
        ("Duration", str),
        ("Date", datetime),
        ("Slides", str),
        ("Recording", str),
        ("Description", str),
    ]
    res = sheet.get(
        spreadsheetId=SPREADSHEET_ID,
        ranges=[f"{SHEET}!{RANGE}"],
        includeGridData=True,
    ).execute()

    sessions = []
    for row in res["sheets"][0]["data"][0]["rowData"]:
        if "values" in row and row["values"][0]:
            session = {}
            for column_index in range(len(COLUMNS)):
                (column, type) = COLUMNS[column_index]
                session[column] = get_value_row(
                    row["values"][column_index]
                    if index_in_list(row["values"], column_index)
                    else None,
                    type,
                )
                if COLUMNS[column_index][0] == "Recording":
                    session["Link"] = get_id(session[column])

            sessions.append(session)

    # Sort sessions by date
    sessions.sort(key=lambda x: x["Date"]["Object"], reverse=True)

    return render_template("masterclasses.html", sessions=sessions)
