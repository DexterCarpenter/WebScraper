#
# Web Scraper
# Version: 9

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
from twilio.rest import TwilioRestClient

#Trilio
account_sid = 'AC008334640b4e1ecb23f9843b8eceb968'
auth_token = '535118992f9f79941eb62c533b835a38'
twilio_phone_number = '+19714071594'
my_phone_number = '+15039649532'

#variables
global tagcountnow
global tagcountold
global scrape_interval



print ''
print "Press 'Ctrl + C' to exit the Scraper"

# specify the url
print 'Enter what website you want to scrape:'
quote_page = raw_input()
try:
	webUrl = urllib2.urlopen(quote_page)
	if(webUrl.getcode() == 200):
		quote_page = '%s' %quote_page
	else:
		code = webUrl.getcode()
except Exception:
	quote_page = raw_input('Enter a valid website: ')

print ''

print 'How often do you want to scrape the webpage? (seconds)'
scrape_interval = raw_input()

print ''

print 'The Scraper will check the number of tags in the webpage.'
print 'The Scraper will display "Change!" if the number of tags has changed from the previous scan.'

print ''

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


def twilio(): 
    
    # query the website and return the html to the variable page
	page = urllib2.urlopen(quote_page)

	# parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
    
    free_food = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

    if free_food:
        body = 'Free Postmates!\n\n' + '\n'.join(free_food)
        client = TwilioRestClient(account_sid, auth_token)
        client.messages.create(
            body=body,
            to=my_phone_number,
            from_=twilio_phone_number
        )

if __name__ == "__main__":
        twilio()

while True:
	
    if __name__ == "__main__":
        scraper()
    
    time.sleep(float(scrape_interval))

































