import urllib.request

from googleDocs_post import upload_files

url = 'https://www.52shuku.vip/chongsheng/15386.html'

# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
# Read the content as string decoded with ISO-8859-1
data = infile.decode('ISO-8859-1')

print(data)  # Print the data to the screen

import config
from apiclient.discovery import build

def printChildren(parent):
  param = {"q": "'" + parent + "' in parents and mimeType != 'application/vnd.google-apps.folder'"}
  result = service.files().list(**param).execute()
  files = result.get('files')

  for afile in files:
    print('File {}'.format(afile.get('name')))

API_KEY = config.gc_key # get from API->Credentials page in console.cloud.googl.com
FOLDER_ID = config.FOLDER # NOTE: folder must be publicly visible when using an API key.
service = build('drive', 'v3', developerKey=API_KEY)
printChildren(FOLDER_ID)

from googleapiclient.discovery import build
api_key = config.gc_key  # Please set your API key

api_service_name = "drive"
api_version = "v3"
youtube = build(api_service_name, api_version, developerKey=api_key)
request = upload_files("file")
response = request.execute()
print(response)