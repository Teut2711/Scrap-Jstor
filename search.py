
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


def search(driver, search_text):

    ele = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "searchBox")))
    ele.send_keys(search_text)
    driver.find_element_by_xpath("//button[@class='button']").click()
