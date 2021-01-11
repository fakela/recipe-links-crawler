from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
import re


PATH = "/Users/favourkelvin/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.allrecipes.com/search/results/?wt=meatballs&page=1")
# save_cookies(driver, cookies_location)
time.sleep(3)
# find all recipes in the page

incategory = driver.find_elements_by_class_name("fixed-recipe-card")
#Generate a list of links for each and every recipe
links = []
for i in range(len(incategory)):
	item = incategory[i]
	#get the href property
	a = item.find_element_by_tag_name("h3").find_element_by_tag_name("a").get_property("href")
	#Append the link to list links
	links.append(a)



all_details = []
# loop through each link to acces each recipe page
for link in links:
	# get one url
	driver.get(url=link)
	# title of the recipe
	elements = driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div[1]/div/h1")
	Title = [el.text for el in elements]
	# author of the recipe
	elements = driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div[4]/div/span/span/a")
	author = [el.text for el in elements]
	# ingredients
	elements = driver.find_elements_by_xpath("//*[@id='ar-calvera-app']/section[1]/fieldset/ul/li/label/span/span")
	ingredient = [el.text for el in elements]
	
	
	print(Title, author, ingredient)
	
