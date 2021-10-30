import gspread_dataframe as gd
import gspread
import glob
if glob.glob("config.py"):
    import config
else:
    import github_config as config
import urllib.request

url = 'https://www.shubaow.net/127_127391/'

# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url)
infile = urllib.request.urlopen(page).read()
# Read the content as string decoded with ISO-8859-1
data = infile.decode('ISO-8859-1')

print(data)  # Print the data to the screen
