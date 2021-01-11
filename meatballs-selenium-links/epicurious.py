import pickle
import pprint
import time

from selenium import webdriver

# Initial load of the domain that we want to save cookies for
chrome = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
chrome.get("https://www.epicurious.com/search/meatballs")
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# #gets the different meatballs recipe name
elements = chrome.find_elements_by_css_selector(".view-complete-item")
cardTitle = [el.text for el in elements]

# #gets the different meatballs recipe urls/links
linkUrls = chrome.find_elements_by_css_selector(".view-complete-item")
linkUrls = [el.get_attribute("href") for el in elements]


print(cardTitle, linkUrls)

