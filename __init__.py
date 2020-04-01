from urllib.parse import urljoin
import json

from time import sleep
import re
import requests


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from itertools import repeat

import _scrap_this_url


class scrapJstor():

    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        'browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', './')
    profile.set_preference("pdfjs.disabled", "true")
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/pdf")

    driver = webdriver.Firefox()
    articles = dict()
    strange = 0
    login = r"https://www.jstor.org/action/showLogin"

    def __init__(self):

        self.links_page = None
        self.driver.get(self.login)
        input("Proceed? ")
        self.search()
        self.links_page = self.driver.current_url
        self.all_docs_links = [self.page_link(i)
                              for i in self.driver.find_elements_by_xpath(
            "//li[@class='row result-item']")]
        self.feed_dict()

    def search(self, search_text="leadership and organizational behaviour"):
        self.search_text = search_text
        self.driver.find_element_by_css_selector(
            "input[name='Query']").send_keys(
                "leadership and organizational behaviour")
        self.driver.find_element_by_xpath("//button[@class='button']").click()

    def feed_dict(self):
        for k, url in enumerate(self.all_docs_links):
            _scrap_this_url.scrape(self, k, url)
            self.get_back()

    def page_link(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url

    def save_cookies(self):
        self.cookies = self.driver.get_cookies()

    def get_back(self):
        self.driver.get(self.links_page)


obj = scrapJstor()

with open("files_copy.json", "w") as f:
    json.dump(obj.articles, f, default=list)
