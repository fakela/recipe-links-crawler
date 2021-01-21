from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
import re


PATH = "/Users/favourkelvin/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
# parse the page source using get() function
driver.get("https://www.allrecipes.com/search/results/?wt=meatballs&page={}")


#next_button = driver.find_element_by_class_name("next").find_element_by_tag_name("a").click()
all_details = []
for c in range(1, 6):
    try:
        # get the page
        driver.get(
            "https://www.allrecipes.com/search/results/?wt=meatballs&page={}".format(c))
        print(
            "https://www.allrecipes.com/search/results/?wt=meatballs&page={}".format(c))

        incategory = driver.find_elements_by_class_name("fixed-recipe-card")

        links = []
        for i in range(len(incategory)):
            item = incategory[i]
            # get the href property
            a = item.find_element_by_tag_name(
                "h3").find_element_by_tag_name("a").get_property("href")
            # Append the link to list links
            links.append(a)

        # Lets loop through each link to acces the page of each recipe
        recipe = []
        for link in links:
            
            # get one recipe url
            driver.get(url=link)
            # title of the recipe
            elements = driver.find_elements_by_xpath(
                "/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div[1]/div/h1")
            title = [el.text for el in elements]

            # author
            elements = driver.find_elements_by_xpath(
                "/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[1]/div[4]/div/span/span/a")
            author = [el.text for el in elements]

            # ingredient
            elements = driver.find_elements_by_xpath(
                "//*[@id='ar-calvera-app']/section[1]/fieldset/ul/li/label/span/span")
            ingredient = [el.text for el in elements]

            r = (title, author, ingredient)
            # append r to all details
            recipe.append(r)
        
        
    except:
        driver.close()
    print(recipe)    
   
