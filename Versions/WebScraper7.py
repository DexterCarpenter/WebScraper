#
# Web Scraper
# Version: 7

"""
cd C:\Users\Dexter Carpenter\Documents\GitHub\WebScraper\environment

c:\Python27\Scripts\virtualenv.exe -p C:\Python27\python.exe .lpvenv

.lpvenv\Scripts\activate

# on at home computer:

cd C:\Users\dexte\Documents\GitHub\WebScraper\environment

"""

# import libraries
import urllib2
from bs4 import BeautifulSoup
import time

#variables
global tagcountnow
global tagcountold



print ""
print "Press 'Ctrl + C' to exit the Scraper"
# specify the url
quote_page = raw_input('Enter what website you want to scrape: ')
try:
	webUrl = urllib2.urlopen(quote_page)
	if(webUrl.getcode() == 200):
		quote_page = '%s' %quote_page
	else:
		code = webUrl.getcode()
except Exception:
	quote_page = raw_input('Enter a valid website: ')

print ""

print "The Scraper will check the number of tags in the webpage."
print "The Scraper will display 'Change!' if the number of tags has changed from the previous scan."
print "The Scraper will scan every 10 seconds"

print ""

print 'Scraping...'

#get the initial count for tags
def initial():
	global tagcountnow
	global tagcountold
	
	# query the website and return the html to the variable page
	page = urllib2.urlopen(quote_page)

	# parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')

	#find number of tags
	tagcountold = len(soup.find_all())

if __name__ == "__main__":
        initial()

def scraper():
	global tagcountnow
	global tagcountold
	
    # query the website and return the html to the variable page
	page = urllib2.urlopen(quote_page)
    
    # parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
	
	#find number of tagss
	tagcountnow = len(soup.find_all())
	
	if tagcountnow == tagcountold:
		print 'No Change'
	elif tagcountnow != tagcountold:
		print 'Change!'
	
	tagcountold = tagcountnow

while True:
    
    if __name__ == "__main__":
        scraper()
    
    time.sleep(10)

































