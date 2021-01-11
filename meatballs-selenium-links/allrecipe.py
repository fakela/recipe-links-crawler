import pickle
import pprint
import time

from selenium import webdriver



chrome = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
chrome.get("https://www.allrecipes.com/search/results/?wt=meatballs")
time.sleep(3)

#gets the different meatballs recipe name
elements = chrome.find_elements_by_css_selector("span.fixed-recipe-card__title-link")
cardTitle = [el.text for el in elements]

#gets the different meatballs recipe urls/links
elements = chrome.find_elements_by_xpath("//*[@id='fixedGridSection']/article/div[2]/h3/a")
linkUrls = [el.get_attribute("href") for el in elements]



print(cardTitle, linkUrls)

