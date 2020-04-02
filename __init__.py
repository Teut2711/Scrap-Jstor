from urllib.parse import urljoin
import json

from time import sleep
import re
import requests


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from itertools import repeat

#import _scrap_this_url


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
        #input("Proceed? ")
        self.log_me_in()
        self.search()
        #self.links_page = self.driver.current_url
        self.scrape_all_links()
        # self.feed_dict()

    def log_me_in(self):
        ele = self.driver.find_element_by_xpath("//input[@name='login']")
        ele.click()
        for i in "apple2711":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath("//input[@name='password']")
        ele.click()
        for i in "abcdefg0":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath("//input[@name='submit']").click()

    def search(self, search_text="leadership and organizational behaviour"):
        self.search_text = search_text
        ele = self.driver.find_element_by_css_selector(
            "input[name='Query']")
        for i in "leadership and organizational behaviour":
            ele.send_keys(i)
        self.driver.find_element_by_xpath("//button[@class='button']").click()

    def scrape_all_links(self):

        for k, row in enumerate(self.driver.find_elements_by_xpath(
                "//li[@class='row result-item']")):
            try:  # try find dwnld btn
                doc = row.find_element_by_xpath(
                    ".//a[@class='pdfLink button']")
            except NoSuchElementException:  # exception do nothing
                pass
            
            else:    
                self.articles[k+1] = {"download_link": doc}
            finally:  # add lnk nd data
                self.articles[k+1] = {"site_link": self.page_link(row)}
                self.articles[k+1].update(self.scrap_info(row))

    def scrap_info(self, ele):
        return {"TITLE": self.title(ele),
                "AUTHORS": self.authors(ele),
                "CITATION": self.citation(ele),
                "TOPICS": self.topics(ele)
                }

    def title(self, ele):

        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        name = current_tag.text
        href = current_tag.get_attribute("href")
        return name

    def authors(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='contrib']//descendant::a")
        authors = [j.text for j in current_tag]
        return authors

    def citation(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='src break-word']")
        citation = current_tag.text
        return citation

    def topics(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='topic-evaluation-pane mtm']//descendant::a")
        tags = [j.text for j in current_tag]
        return tags

    # def feed_dict(self):
    #     for k, url in enumerate(self.all_docs_links):
    #         _scrap_this_url.scrape(self, k, url)
    #         self.get_back()

    def page_link(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url

    # def save_cookies(self):
    #     self.cookies = self.driver.get_cookies()

    # def get_back(self):
    #     self.driver.get(self.links_page)


obj = scrapJstor()

with open("files_copy.json", "w") as f:
    json.dump(obj.articles, f, default=list)
