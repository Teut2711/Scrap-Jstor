from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, username, password):
    feed_username(driver, username)
    feed_password(driver, password)
    submit(driver)


def feed_username(driver, username):
    ele = driver.find_element_by_xpath("//input[@name='login']")
    ele.click()
    for i in username:
        ele.send_keys(i)


def feed_password(driver, password):
    ele = driver.find_element_by_xpath("//input[@name='password']")
    ele.click()
    for i in password:
        ele.send_keys(i)


def submit(driver):
    ele = driver.find_element_by_xpath(
        "//input[@name='submit']")
    ele.click()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(ele))
