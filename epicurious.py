import pickle
import pprint
import time

from selenium import webdriver

driver = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float 
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int 
        driver.add_cookie(cookie)

def delete_cookies(driver, domains=None):
    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()



cookies_location = "/Users/favourkelvin/Documents/recipe-links-crawler/cookies.txt"

# Initial load of the domain that we want to save cookies for
chrome = webdriver.Chrome('/Users/favourkelvin/Downloads/chromedriver')
chrome.get("https://www.epicurious.com/search/meatballs")
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
save_cookies(chrome, cookies_location)

# #gets the different meatballs recipe name
elements = chrome.find_elements_by_css_selector(".view-complete-item")
cardTitle = [el.text for el in elements]

# #gets the different meatballs recipe urls/links
linkUrls = chrome.find_elements_by_css_selector(".view-complete-item")
linkUrls = [el.get_attribute("href") for el in elements]


print(cardTitle, linkUrls)

