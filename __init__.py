from urllib.parse import urljoin
from time import sleep
from base64 import b64decode

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import json
import requests
import img2pdf
import re


from .login import Login


class Jstor():

    def __init__(self, username="apple2711", password="abcdefg0", search="something"):
        setattr(self, username, username)
        setattr(self, password, password)
        self.complete_the_task()


    def complete_the_task(self):
        Login(self.username, self.password)
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
