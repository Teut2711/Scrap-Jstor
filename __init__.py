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

from login import Login


class Jstor(Login):

    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox()
    link = r"https://www.jstor.org/action/showLogin"

    @classmethod
    def browser_settings(cls, download_dir=os.getcwd(), open_pdf_in_browser=False):
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
        super(Login, self).__init__()
        #super(Search, self).__init__(link)

obj = Jstor("apple2711", "abcdefg0")

# with open("files_copy.json", "w") as f:
#     json.dump(obj.articles, f, default=list)
