from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import os
from dotenv import load_dotenv

load_dotenv()

client_secret_file = os.getenv('CLIENT_SECRET_FILE')
api_name = os.getenv('API_NAME')
api_version = os.getenv("API_VERSION")
scopes = os.getenv("SCOPES")

folder_id = os.getenv("FOLDER_ID")
mime_type = 'image/jpeg'

service = Create_Service(client_secret_file, api_name, api_version, scopes)

def uploadFile(file_name, local_image_path):
    try:
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload('{0}/{1}'.format(local_image_path, file_name), mimetype=mime_type)

        service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
        ).execute()

        return True
    except:
        return False


