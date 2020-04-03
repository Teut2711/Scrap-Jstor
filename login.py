from selenium import webdriver
import os

driver = webdriver.Firefox()
articles = dict()
strange = 0
login = r"https://www.jstor.org/action/showLogin"
total_articles_scraped = 0
total_articles_to_scrape = 60


class Login:
    def __init__(self, username, password):
        self.browser_options()
        self.log_me_in()

    @staticmethod
    def browser_options(download_folder=os.getcwd()):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', os.getcwd())
        profile.set_preference("pdfjs.disabled", "true")
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf")

    def log_me_in(self):
        ele = self.driver.find_element_by_xpath("//input[@name='login']")
        ele.click()
        for i in "apple2711":
            ele.send_keys(i)
        
    def feed_password(self):
        ele = self.driver.find_element_by_xpath("//input[@name='password']")
                ele.click()
                for i in "abcdefg0":
                    ele.send_keys(i)
                ele = self.driver.find_element_by_xpath(
                    "//input[@name='submit']").click()
    
    def submit(self):                 
