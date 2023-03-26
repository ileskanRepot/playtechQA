from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from datetime import datetime
from time import sleep

# If set to True it does as bonus task descripted
useCoords = False

textToSearch = "Development QA Engineer (Intern)"

scrollAmount = 50
timeout = 5

with webdriver.Chrome() as driver:
    
    driver.get("https://playtech.ee")
    
    # Accept cookies
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((
            By.CLASS_NAME, "custom-btn.text-nowrap.is-simple.ml-xl-2.mr-3.mr-xl-0.mb-2"))).click()
    
    # Get all element with same class
    internsshipEList = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((
            By.CLASS_NAME, "d-block.font-size-sm.font-weight-bold.text-uppercase.styled-link.mb-1.mb-xl-0.mr-sm-3.mr-xl-4")))
    
    # Filter same class list
    for o in internsshipEList:
        if o.text == "INTERNSHIP":
            internsshipE = o

    internsshipE.click()

    didFind = False
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((
                By.XPATH,"//*[contains(text(),\""+textToSearch+"\")]")))
        didFind = True
    except TimeoutException:
        print("'"+textToSearch+"'Was not in page")

    with open("logs.txt",'a') as f:
        f.write(str(datetime.now())+" :"+textToSearch)
        if didFind:
            f.write(" Was found\n")
        else: 
            f.write(" Was not found\n")