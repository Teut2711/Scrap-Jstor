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

from .login import Login


class Jstor():

    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox()
    link = r"https://www.jstor.org/action/showLogin"
    @classmethod
    def browser_settings(cls, username=None, password=None,
                         download_dir=os.getcwd(), open_pdf_in_browser=False):
        if username and password:
            cls.profile.set_preference('browser.download.dir', download_dir)
            cls.profile.set_preference(
                "pdfjs.disabled", not(open_pdf_in_browser))
            cls.profile.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/pdf")
            cls(username=username, password=password)
        else:
            raise ValueError("Username and Password cannot be type 'None'")

    def __init__(self, username="apple2711", password="abcdefg0",
                 search="something"):
        self.browser_settings(username=username, password=password)
        setattr(self, username, username)
        setattr(self, password, password)
        Login(self, link=self.link)

    def complete_the_task(self):
        Login.login(self.username, self.password)
        Search(self.search_text)
        Extract

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.password

    @property
    def search_text(self):
        return self.search_text

    @username.setter
    def usename(self, username):
        self.username = username

    @password.setter
    def password(self, password):
        self.password = password

    @search_text.setter
    def search_text(self, search_text):
        self.search_text = search_text

    def log_me_in(self):

        Login()

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
