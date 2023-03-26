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

timeout = 15

with webdriver.Chrome() as driver:
    
    driver.get("https://playtech.ee")
    sleep(5)
    driver.find_element(By.CLASS_NAME, "custom-btn.text-nowrap.is-simple.ml-xl-2.mr-3.mr-xl-0.mb-2").click()
    internsshipE = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((
            By.XPATH, '//a[@href="/internship"]')))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    sleep(timeout)
    loc = internsshipE.location_once_scrolled_into_view
    siz = internsshipE.size
    wMin, hMin = loc["y"], loc["x"]

    wMax = wMin + siz["width"]
    hMax = hMin + siz["height"]
    print("loc",loc)
    print("siz",siz)
    print(hMax,wMax)

    crash()
    sleep(100)
    if useCoords:
        ac = ActionChains(driver)
        ac.move_by_offset(wMax, hMax)
        ac.click()
        ac.perform()
        
        driver.execute_script(f"window.scrollTo(0, {hMax});")
    else:
        # print(internsshipE.tag_name)
        # print(hMax)
        driver.refresh()

        internsshipE.click()


    print(loc)
    sleep(100)

    # print(driver.get_window_size()) # GET WINDOW SIZE
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))