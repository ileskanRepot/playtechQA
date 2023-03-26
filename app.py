from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

# If set to True it does as bonus task descripted
useCoords = False

textToSearch = "get a personal mentor, who will help and support you during the internship period"

timeout = 5

with webdriver.Chrome() as driver:


    driver.get("https://playtech.ee")
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((
            By.CLASS_NAME, "custom-btn.text-nowrap.is-simple.ml-xl-2.mr-3.mr-xl-0.mb-2"))).click()
    internsshipEList = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((
            By.CLASS_NAME, "d-block.font-size-sm.font-weight-bold.text-uppercase.styled-link.mb-1.mb-xl-0.mr-sm-3.mr-xl-4")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for o in internsshipEList:
        if o.text == "INTERNSHIP":
            internsshipE = o

    internsshipE.click()
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((
                By.XPATH,"//*[contains(text(),\""+textToSearch+"\")]")))
    except TimeoutExpection:
        print("TEXT:",textToSearch,"Was not in page")
sleep(100)