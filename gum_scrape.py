# Reads a csv file of listing URLs and scrapes data of each in a csv output

import selenium, time, csv

from urllib.request import Request as uReq, urlopen
from selenium import webdriver

browser = webdriver.Chrome()

my_url = 'https://www.gumtree.com.au/s-ad/melbourne-cbd/property-for-rent/fully-furnished-luxurious-studio-apartment-in-cbd/1262691265'

# Grabs webpage
webpage = urlopen(uClient).read()
page_soup = soup(webpage, "html.parser")

# Pushes 'Show More' button on description and 'Show All' button in details

but_more = driver.find_element_by_css_selector("input#passwd-id")
but_show = driver.find_element_by_css_selector("input#passwd-id")

