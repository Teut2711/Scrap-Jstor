from urllib.parse import urljoin
from templates import GeneralDoc
from utils import helper_try_except
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests


class FREE(GeneralDoc):
    def __init__(self, driver, row):
        super().__init__(row)
        self.PDF = self.makePDF(driver, row)
        self.attributes["PDF"] = self.makePDF(driver,
                                              self.title, row)

    def makePDF(self, driver, filename, row):

        @helper_try_except
        def scrape_download_link():

            doc = row.find_element_by_xpath(
                ".//a[@class='pdfLink button']").get_attribute("href")

            return urljoin(driver.current_url, doc)

        with open(f"{filename}.pdf") as f:
            f.write(requests.get(scrape_download_link(),
                                 cookies=driver.get_cookies()
                                 ).content)

        # ActionChains(driver).key_down(Keys.CONTROL).send_keys(
        #     "C").key_up(Keys.CONTROL).perform()
        # ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
