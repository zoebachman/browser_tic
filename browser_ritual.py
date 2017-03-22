#selenium webdriver that opens up the browser and goes to email, scrolls, then facebook, scrolls, twitter, scrolls


import time, random, ConfigParser
from selenium import webdriver
from bs4 import BeautifulSoup


## Initiate browser

browser = webdriver.Chrome()
browser.set_window_size(980,1820)
browser.set_window_position(200,200)

## URLs
gmail_url = 'http://gmail.com'
facebook_url ='facebook.com'


#gmail
browser.get(gmail_url)
page = BeautifulSoup(browser.page_source, "lxml")
time.sleep(random.uniform(0.5,1.4)) #make this longer?
# browser.get(signinUrl) *need login info*


#facebook
browser.get(facebook_url)
page = BeautifulSoup(browser.page_source, "lxml")
time.sleep(random.uniform(0.5,1.4))

browser.close()