# Selenium allows us to interact with HTML Code from any website
# Step 1: get pip working (comes with python as default)
# pip3 is installed on my system
# Step 2: install selenium (using pip)
# $ pip install selenium (we must install selenium to our virtual environment)
# The next line imports selenium to our python project
import selenium
# The next line imports the webdriver library
from selenium import webdriver
# Next impirt the chrome driver service
from selenium.webdriver.chrome.service import Service
# This adds the abillity to configure options on the chrome web driver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# Import keys options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Configure some options for our browser
options = Options()
options.add_experimental_option("detach", True)
# creates the webdriver without the need to install the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# define a website object linked to where we want to pull data from,
# we create the object and save it at compile time
website = 'https://www.apps.miamioh.edu/courselist/'
# driver opens the website
driver.get(website)


# Data extraction --------------------------------------------------

# common to access html element by id, name, or class name (best to worst) 

# "alternative delivery types checkbox" (all must be checked) ------
# Face to Face Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onlineF2FFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"onlineF2FFilter").click()

# Online Sync Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onlineSyncFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"onlineSyncFilter").click()

# Online Async Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onlineAsyncFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"onlineAsyncFilter").click()

# Hybrid Sync Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "hybridSyncFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"hybridSyncFilter").click()

# Hybrid Async Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "hybridAsyncFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"hybridAsyncFilter").click()

# IVDL Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ivdlFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"ivdlFilter").click()

# Study Abroad Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "studyAbroadFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"studyAbroadFilter").click()

# Study Away Checkbox
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "studyAwayFilter"))
    )
except:
    driver.quit()

driver.find_element(By.ID,"studyAwayFilter").click()

# END ADT Checkbox -----------------------------------------------------
# Term, Campus, Subject, Attribute dropdowns ---------------------------









# END dropdowns
# Click advanced search button and wait for options to appear

# Loop to search each CRN, Scrape data into a vector

# quit the driver when finished to avoid windows staying open (add delay)
#driver.quit()

# next get the current date from python
from datetime import date
date = date.today()
# gives options for date.year, date.month, date.day
print(date.year)


#look into microsoft azure functions to call the webScraping function each day