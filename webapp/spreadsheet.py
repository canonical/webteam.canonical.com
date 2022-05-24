import os
import hashlib
import tempfile
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "client.json"
PRIVATE_KEY_ID = os.getenv("PRIVATE_KEY_ID")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")


class MissingCredential(Exception):
    pass


class DiscoveryCache:
    """
    Unix file-based cache for use with the API Discovery service
    See https://github.com/googleapis/google-api-python-client/issues/325#issuecomment-419387788
    """  # noqa

    def filename(self, url):
        return os.path.join(
            tempfile.gettempdir(),
            "google_api_discovery_" + hashlib.md5(url.encode()).hexdigest(),
        )

    def get(self, url):
        try:
            with open(self.filename(url), "rb") as f:
                return f.read().decode()
        except FileNotFoundError:
            return None

    def set(self, url, content):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(content.encode())
            f.flush()
            os.fsync(f)
        os.rename(f.name, self.filename(url))


def get_sheet():
    if not PRIVATE_KEY_ID:
        raise MissingCredential("PRIVATE_KEY_ID is missing")

    if not PRIVATE_KEY:
        raise MissingCredential("PRIVATE_KEY is missing")

    service_account_info = {
        "type": "service_account",
        "project_id": "roadmap-270011",
        "private_key_id": PRIVATE_KEY_ID,
        "private_key": PRIVATE_KEY,
        "client_email": "specs-reader@roadmap-270011.iam.gserviceaccount.com",
        "client_id": "112404606310881291739",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": (
            "https://www.googleapis.com/oauth2/v1/certs"
        ),
        "client_x509_cert_url": (
            "https://www.googleapis.com/robot/v1/metadata"
            "/x509/specs-reader%40roadmap-270011.iam.gserviceaccount.com"
        ),
    }

    creds = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds, cache=DiscoveryCache())
    sheet = service.spreadsheets()

    return sheet
