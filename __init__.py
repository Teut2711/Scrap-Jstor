from urllib.parse import urljoin
from time import sleep
from base64 import b64decode

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


import json
import requests
import img2pdf
import re

import os

from login import login

from search import search
from extractallrows import extractallrows


class Jstor:

    link = r"https://www.jstor.org/action/showLogin"
    search_text = "leadership and organizational behaviour"

    @classmethod
    def browser_start_FireFox(cls, download_dir=os.getcwd(),
                              open_pdf_in_browser=False):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', download_dir)
        profile.set_preference(
            "pdfjs.disabled", not(open_pdf_in_browser))
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        cls.driver = webdriver.Firefox(firefox_profile=profile)

    def __init__(self, username="apple2711", password="abcdefg0"):
        Jstor.browser_start_FireFox()
        self.username = username
        self.password = password
        self.driver.get(self.link)
        login(self.driver, self.username, self.password)
        search(self.driver, self.search_text)
        self.all_docs = extractallrows(self.driver)


obj = Jstor("apple2711", "abcdefg0")

# with open("files_copy.json", "w") as f:
#     json.dump(obj.articles, f, default=list)
