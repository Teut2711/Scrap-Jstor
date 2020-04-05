def login(driver, username, password):
    driver.feed(driver, id)
    driver.feed(driver, password)
    driver.submit(driver)


def feed_id(driver, username):
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
    driver.find_element_by_xpath(
        "//input[@name='submit']").click()
