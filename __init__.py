from urllib.parse import urljoin
from time import sleep
from base64 import b64decode

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import json
import requests
import img2pdf
import re


from . import free
from . import paid


class Jstor:

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

    def __init__(self, username="apple2711", password="abcdefg0"):
        self.username = username
        self.password = password
        self.log_me_in()
        self.search()

    def log_me_in(self):

        Login.log_me_in()

    def search(self):
        Search.search()
        self.links_page = None
        self.driver.get(self.login)
        self.log_me_in()
        self.search()
        self.scrape_all_links()
        self.user_list = self.ask()
        self.scrap_user_choice()





obj = Jstor()

with open("files_copy.json", "w") as f:
    json.dump(obj.articles, f, default=list)

