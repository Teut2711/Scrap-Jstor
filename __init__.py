from urllib.parse import urljoin
from time import sleep
from base64 import b64decode

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import json
import requests
import img2pdf
import re


class searchJstor:

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
    total_articles_scraped = 0
    total_articles_to_scrape = 60

    def __init__(self):

        self.links_page = None
        self.driver.get(self.login)
        self.log_me_in()
        self.search()
        self.scrape_all_links()
        self.user_list = self.ask()
        self.scrap_user_choice()

    def log_me_in(self):
        ele = self.driver.find_element_by_xpath("//input[@name='login']")
        ele.click()
        for i in "apple2711":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath("//input[@name='password']")
        ele.click()
        for i in "abcdefg0":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath(
            "//input[@name='submit']").click()

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
                self.total_articles_scraped += 1
                if self.total_articles_scraped ==\
                        self.total_articles_to_scrape:
                    return None

            try:
                ele = self.driver.find_element_by_xpath(
                    "//li[@class='pagination-next']/a[@id='next-page']")
            except NoSuchElementException:
                pass
            else:
                ele.click()
                sleep(3)
                self.scrape_all_links()

    def scrap_info(self, ele):
        d = {"TITLE": self.title,
             "AUTHORS": self.authors,
             "CITATION": self.citation,
             "TOPICS": self.topics
             }
        for (key, value) in d.items():
            try:
                d[key] = value(ele)
            except NoSuchElementException:
                d[key] = None
        return d

    def title(self, ele):

        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        name = current_tag.text
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

    def page_link(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url

    def scrap_user_choice():


class FREE:
    def download_pdf(self):
        for i in selected:
            if self.articles[i].get("download_link"):
                self.driver.get(
                    self.articles[i]["download_link"])
            else:
                self.driver.get(
                    self.articles[i]["site_link"])
                self.get_unpaid()

    def get_unpaid(self):
        try:
            ele = self.driver.find_element_by_xpath(
                """//ul[@class='action-buttons mln']/li/a[contains(text(),
                    'Read')][contains(text(), 'Online')]""")
        except NoSuchElementException:
            try:
                return self.scrap_pdf()

            print("See the site")
        else:
            ele.click()

    def scrap_pdf(self):
        try:
            images = []
            while True:
                images.append(self.driver.find_element_by_xpath(
                    """//img[@id='page-scan-container']
                    [contains(@src,'data:image')]""")
                ).get_attribute("src")
                self.driver.find_element_by_xpath(
                    "//span[@aria-label='Next Page']").click()
        except NoSuchElementException:
            pass
        else:
            self.toPDF(images)

    @staticmethod
    def toPDF(file_name, list_of_base64=[]):
        list_of_base64 = [parse_base64(i) for i in list_of_base64]
        with open(f"{file_name}.pdf", "wb") as f:
            f.write(img2pdf.convert(list_of_base64))
        return f"{file_name}.pdf"

        def parse_base64(string):
            if string.startswith("data:image"):
                return b64decode(string.split(",")[1], validate=True)


class PAID(searchJstor):

    def __init__(self):
        self.



obj = searchJstor()

with open("files_copy.json", "w") as f:
    json.dump(obj.articles, f, default=list)


class Login:
   def __init__():
       