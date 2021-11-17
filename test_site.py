import urllib.request

url = 'https://www.52shuku.vip/chongsheng/15386.html'

# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
# Read the content as string decoded with ISO-8859-1
data = infile.decode('ISO-8859-1')

print(data)  # Print the data to the screen
