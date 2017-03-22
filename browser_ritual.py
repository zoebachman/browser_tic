#selenium webdriver that opens up the browser and goes to email, scrolls, then facebook, scrolls, twitter, scrolls


import time, random, ConfigParser
from selenium import webdriver
from bs4 import BeautifulSoup


def getSigninLink(page):
	links = []
	url = ''
	for link in page.find_all('a'):
		role = link.get('id')
		if role:
			if role == "gb_70":
				url = link.get('href')
				print url
	return url

def Main():
	## Read Config file
	config = ConfigParser.ConfigParser()
	try:
		config.read('settings.cfg')
		print "[+] read your settings"
	except:
		print "[-] couldn't read settings"

	

	#Gmail
	# configDomain = config.get('google','domain')
	configEmail = config.get('google','email')
	configPass = config.get('google','psswrd')

	#Facebook
	# facebook_configDomain = config.get('facebook')

	## Initiate browser
	browser = webdriver.Chrome()
	browser.set_window_size(980,1820)
	browser.set_window_position(200,200)

	## URLs
	gmail_url = 'http://gmail.com'
	# facebook_url ='facebook.com'


	#gmail
	browser.get(gmail_url)
	page = BeautifulSoup(browser.page_source, "lxml")
	# signinUrl = 
	time.sleep(random.uniform(0.5,1.4)) #make this longer?
	# browser.get(signinUrl) #create function
	emailElement = browser.find_element_by_id("Email")

	configEmail2 = list(configEmail)
	for i in configEmail2:
		emailElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))

	time.sleep(random.uniform(0.5,1.4))
	emailElement.submit()
	time.sleep(random.uniform(0.5,1.4))
	passElement = browser.find_element_by_id("Passwd")

	configPass2 = list(configPass)
	for i in configPass2:
		passElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))


	time.sleep(random.uniform(0.5,1.4))
	passElement.submit()

	print "[+] Logged in to Google. Will now browse'"
	#scroll through page


	#facebook
	# browser.get(facebook_url)
	# page = BeautifulSoup(browser.page_source, "lxml")
	# time.sleep(random.uniform(0.5,1.4))

	browser.close()

if __name__ == '__main__':
	Main()
