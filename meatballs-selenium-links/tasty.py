import pickle
import pprint
import time

from selenium import webdriver

chrome = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
chrome.get("https://www.edamam.com/recipes/meatballs")
# chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

#gets the different meatballs recipe name
elements = chrome.find_elements_by_css_selector("span.title")
cardTitle = [el.text for el in elements]


#gets the different meatballs recipe urls/links
elements = chrome.find_elements_by_css_selector(".meals-list ul li .object a")
linkTitle = [el.get_attribute("href") for el in elements]


print(cardTitle, linkTitle)
