from urllib.parse import urljoin
from time import sleep
from base64 import b64decode

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import json
import requests
import img2pdf
import re

import os

from jstorScrap.login import Login
from jstorScrap.search import Search
from jstorScrap.extractallrows import ExtractAllRows


class Jstor(Login, Search):

    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox()
    link = r"https://www.jstor.org/action/showLogin"
    search_text = "leadership and organizational behaviour"

    @classmethod
    def browser_settings(cls, download_dir=os.getcwd(),
                         open_pdf_in_browser=False):
        cls.profile.set_preference('browser.download.dir', download_dir)
        cls.profile.set_preference(
            "pdfjs.disabled", not(open_pdf_in_browser))
        cls.profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf")

    def __init__(self, username="apple2711", password="abcdefg0",
                 search="something"):
        Jstor.browser_settings()
        self.driver.get(self.link)
        self.username = username
        self.password = password
        Login.__init__(self)
        Search.__init__(self)
        ExtractAllRows.__init__(self)


obj = Jstor("apple2711", "abcdefg0")

# with open("files_copy.json", "w") as f:
#     json.dump(obj.articles, f, default=list)
