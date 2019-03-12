import urllib
import urllib.request
from bs4 import BeautifulSoup 
import os

def make_soup(url):
    the_page = urllib.request.urlopen(url)
    soup_data = BeautifulSoup(the_page, 'html.parser')
    return soup_data


soup = make_soup("https://www.currency-converter.org.uk/currency-rates/historical/table/USD-INR.html")
div_data = soup.find('div',class_='hfeed')

playerdata = playerdatasaved = ""
for record in div_data.findAll('tr'):
    playerdata=""
    for data in record.findAll('td'):
        playerdata = playerdata + "," + data.text
    playerdatasaved += '\n'+ playerdata[1:]

#header="Day,Date,1USD=,INR,description"
file = open(os.path.expanduser("currency.csv"), "wb")
#file.write(bytes(header, encoding="ascii", errors="ignore"))
file.write(bytes(playerdatasaved, encoding="ascii", errors="ignore"))


