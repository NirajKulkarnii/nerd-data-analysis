import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

credentials_path =os.getenv("DRIVE_CREDENTIALS")
scopes = os.getenv("SCOPES")

def create_drive_service(credentials_path: str = credentials_path, scopes: list = scopes):
    """
    Creates a Google Drive service object using a service account.

    Args:
        credentials_path (str): Path to the service account credentials JSON file.
        scopes (list): A list of scopes for API access.

    Returns:
        drive_service: A Google Drive service object.
    """
    creds = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=[scopes]
    )
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service


def list_files_in_folder(drive_service,folder_id):
    """
    Lists all image files in a given folder and its subfolders in Google Drive.

    Args:
        drive_service(obj): A goole drive service object.
        folder_id (str): The ID of the folder to search within.
        

    Returns:
        list: A list of dictionaries containing image file details (name and webViewLink).
    """
    # List to store image file details
    files_data = []

    # Set up the query to retrieve files from the folder
    query = f"'{folder_id}' in parents and trashed=false"
    page_token = None

    while True:
        # Call the Drive v3 API to list files in the folder
        response = drive_service.files().list(
            q=query,
            spaces='drive',
            fields='nextPageToken, files(id, name, mimeType, webViewLink)',
            pageToken=page_token
        ).execute()

        # Loop through the files in the response
        for file in response.get('files', []):
            # Only add image files to the list (files with MIME type starting with 'image/')
            if file['mimeType'].startswith('image/'):
                    files_data.append({
                        'file_name': file['name'],
                        'file_link': file['webViewLink']
                    })

        # If there is a next page of results, continue fetching
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    return files_data


def list_folders_in_folder(drive_service,parent_folder_id):
    """
    Lists all folders in a given parent folder and its subfolders in Google Drive.

    Args:
        drive_service(obj): A goole drive service object.
        parent_folder_id (str): The ID of the parent folder to search within.

    Returns:
        list: A list of dictionaries containing folder details (name and ID).
    """
    # List to store folder details
    folders_data = []

    # Set up the query to retrieve folders from the specified parent folder
    query = (
        f"'{parent_folder_id}' in parents and "
        f"mimeType='application/vnd.google-apps.folder' and trashed=false"
    )
    page_token = None

    while True:
        # Call the Drive v3 API to list folders in the parent folder
        response = drive_service.files().list(
            q=query,
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token
        ).execute()

        # Loop through the folders in the response
        for folder in response.get('files', []):
            # Store folder details (ID and name)
            folders_data.append({
                'folder_name': folder['name'],
                'folder_id': folder['id']
            })

        # Handle pagination to get all results
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    return folders_data


def download_file_from_drive(file_id, file_name, drive_service, temp_folder='../screenshot_data/temp'):
    """
    Downloads a file from Google Drive using the file ID.

    Args:
        file_id (str): The ID of the file to download from Google Drive.
        file_name (str): The name to save the file as.
        drive_service(obj): A goole drive service object.
        temp_folder (str): The path to the temporary folder to save the file in. Default is './temp'.

    Returns:
        str: The file path where the file was saved.
    """
    # Make a request to download the file content
    request = drive_service.files().get_media(fileId=file_id)
    
    # Save the file to the temp folder
    file_path = os.path.join(temp_folder, file_name)
    
    # Download the file and write its content to the file_path
    with open(file_path, 'wb') as f:
        response, content = drive_service._http.request(request.uri)
        if response.status == 200:
            f.write(content)
        else:
            print(f"Failed to download file. Status code: {response.status}")
    return file_path


def extract_file_id(web_view_link):
    """
    Extracts the file ID from a Google Drive webViewLink.

    Args:
        web_view_link (str): The webViewLink URL of the Google Drive file.

    Returns:
        str: The extracted file ID.
    """
    # The file ID in a webViewLink is between /d/ and /view or the end of the URL
    file_id = web_view_link.split('/d/')[1].split('/')[0]
    return file_id


def get_json_files_from_drive(drive_service, parent_folder_id="1kNSCbyeI5_M3Bhhg3dBkZSN5RJtIkWJ-"):
    """
    Retrieve JSON files from a specified Google Drive folder.

    Args:
        drive_service (googleapiclient.discovery.Resource): Authenticated Google Drive API service instance.
        parent_folder_id (str): The ID of the Google Drive folder to search in (default is a sample folder ID).

    Returns:
        list: A list of files (id, name) that are JSON files in the specified folder.
    """
    
    # Define query to find JSON files in the folder
    query = f"'{parent_folder_id}' in parents and mimeType='application/json'"
    
    try:
        # Fetch the list of files that match the query
        results = drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])
        
        # Return the list of JSON files found
        return files

    except Exception as e:
        # Handle any errors that occur during the API call
        print(f"An error occurred while retrieving files: {e}")
        return []
