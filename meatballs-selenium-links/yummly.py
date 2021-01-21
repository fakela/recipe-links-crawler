import pickle
import pprint
import time

from selenium import webdriver


chrome = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
chrome.get("https://www.yummly.com/recipes?q=meatballs&taste-pref-appended=true")
time.sleep(3)

# #gets the different meatballs recipe name
elements = chrome.find_elements_by_css_selector(".card-title")
cardTitle = [el.text for el in elements]

# #gets the different meatballs recipe urls/links
elements = chrome.find_elements_by_css_selector(".w-full")
linkUrls = [el.get_attribute("href") for el in elements]


print(cardTitle, linkUrls)
