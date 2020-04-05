
def search(driver, search_text):
    ele = driver.find_element_by_css_selector(
        "input[name='Query']")
    for i in search_text:
        ele.send_keys(i)
    driver.find_element_by_xpath("//button[@class='button']").click()
