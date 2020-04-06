from selenium import webdriver
import json
import os

from login import login
from search import search
from extractallrows import extractallrows
from utils import path


for i in os.listdir(path):
    if i.endswith(".pdf"):
        os.remove(os.path.join(path, i))


class Jstor:

    link = r"https://www.jstor.org/action/showLogin"
    search_text = "leadership and organizational behaviour"

    @classmethod
    def browser_start_FireFox(cls, download_dir=path,
                              open_pdf_in_browser=False):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
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
        self.driver.close()


obj = Jstor("apple2711", "abcdefg0")

with open(os.path.join(path, "files_copy.json"), "w") as f:
    json.dump([i.attributes for i in obj.all_docs], f, default=list)
