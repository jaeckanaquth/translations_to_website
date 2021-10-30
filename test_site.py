import gspread_dataframe as gd
import gspread
import config
import urllib.request

url = 'https://www.mbtxt.la/go/79041/'

# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
# Read the content as string decoded with ISO-8859-1
data = infile.decode('ISO-8859-1')

print(data)  # Print the data to the screen

gc = gspread.service_account(filename="service_account.json")
sht1 = gc.open_by_key('AIzaSyBoF74r7zXL_Dl4UueSX5CoE6XMv-0EHMA')
sh = gc.create('A new spreadsheet')
wks = gc.open('A new spreadsheet').sheet1
wks.update('A1', [[1, 2], [3, 4]])


# Connecting with `gspread` here

ws = gc.open('QuthTranslations')
spreadsheet = gc.open("The name of your spreadsheet")
worksheet = spreadsheet.add_worksheet(title="A worksheet", rows="100", cols="5")
existing = gd.get_as_dataframe(ws)
updated = existing.append(your_new_data)
gd.set_with_dataframe(ws, updated)
