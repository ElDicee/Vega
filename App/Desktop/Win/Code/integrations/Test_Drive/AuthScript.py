from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


creds = None
if creds is None:
    flow = InstalledAppFlow.from_client_secrets_file("client_Secret.json", scopes=["https://www.googleapis.com/auth/drive"])
    creds = flow.run_local_server(port=0)
service = build("drive", "v3", credentials=creds)

result = service.files().list(q="'root' in parents", fields="nextPageToken, files(id, name)").execute()
items = result.get("files", [])
for item in items:
    print(item["name"], item["id"])