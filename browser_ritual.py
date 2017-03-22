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

	
	## Initiate browser
	browser = webdriver.Chrome()
	browser.set_window_size(980,2080)
	browser.set_window_position(200,200)

	#Gmail
	# gmail_url = 'http://gmail.com'
	# gmail_configEmail = config.get('google','email')
	# gmail_configPass = config.get('google','psswrd')


	# browser.get(gmail_url)
	# gmail_page = BeautifulSoup(browser.page_source, "lxml")
	# time.sleep(random.uniform(0.5,1.4)) 
	# gmail_emailElement = browser.find_element_by_id("Email")

	# gmail_configEmail2 = list(gmail_configEmail)
	# for i in gmail_configEmail2:
	# 	gmail_emailElement.send_keys(i)
	# 	time.sleep(random.uniform(0,0.1))

	# time.sleep(random.uniform(0.5,1.4))
	# gmail_emailElement.submit()
	# time.sleep(random.uniform(0.5,1.4))
	# gmail_passElement = browser.find_element_by_id("Passwd")

	# gmail_configPass2 = list(gmail_configPass)
	# for i in gmail_configPass2:
	# 	gmail_passElement.send_keys(i)
	# 	time.sleep(random.uniform(0,0.1))


	# time.sleep(random.uniform(0.5,1.4))
	# gmail_passElement.submit()

	# print "[+] Logged in to Google. Will now browse'"
	#scroll through page




	#Facebook
	facebook_url ='http://www.facebook.com'
	facebook_configEmail = config.get('facebook','email')
	facebook_configPass = config.get('facebook','psswrd')


	browser.get(facebook_url)
	facebook_page = BeautifulSoup(browser.page_source, "lxml")
	time.sleep(random.uniform(0.5,1.4)) 
	facebook_emailElement = browser.find_element_by_id("email")

	facebook_configEmail2 = list(facebook_configEmail)
	for i in facebook_configEmail2:
		facebook_emailElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))

	time.sleep(random.uniform(0.5,1.4))
	facebook_passElement = browser.find_element_by_id("pass")
	facebook_configPass2 = list(facebook_configPass)
	for i in facebook_configPass2:
		facebook_passElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))


	time.sleep(random.uniform(0.5,1.4))
	facebook_passElement.submit()

	print "[+] Logged in to Facebook. Will now browse'"
	#scroll through page

	browser.close()

if __name__ == '__main__':
	Main()
