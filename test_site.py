import github_config as config
import urllib.request

url = 'http://www.jjwxc.net/onebook.php?novelid=3046784'

# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
# Read the content as string decoded with ISO-8859-1
data = infile.decode('ISO-8859-1')

print(data)  # Print the data to the screen
