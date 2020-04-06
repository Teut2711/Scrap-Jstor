from img_2_pdf import toPDF
from templates import GeneralDoc
from string import punctuation
import os
from selenium.common.exceptions import NoSuchElementException


class PAID(GeneralDoc):

    def __init__(self, driver, row):
        super().__init__(row)

    def user_opted(self, driver):
        if os.path.exists(self.clean_title(self.title)+".pdf"):
            print("File Already exists")
        else:
            if self.title:
                driver.get(self.pagelink)

                if self.try_read_online(driver):
                    self.PDF = toPDF(self.clean_title(self.title),
                                     self.download_all_base64(driver))
                    self.attributes["PDF"] = self.PDF

                elif self.try_pdf_auto_open(driver):
                    self.PDF = toPDF(self.clean_title(self.title),
                                     self.download_all_base64(driver))
                    self.attributes["PDF"] = self.PDF
                else:
                    print("Check Site")

    def try_read_online(self, driver):
        try:
            ele = driver.find_element_by_xpath(
                """//ul[@class='action-buttons mln']/li/a[contains(text(),
                    'Read')][contains(text(), 'Online')]""")
        except NoSuchElementException:
            pass
        else:
            ele.click()
            self.try_pdf_auto_open(driver)
            return True

    def try_pdf_auto_open(self, driver):
        try:
            driver.find_element_by_xpath(
                "//img[@id='page-scan-container'][contains(@src,'data:image')]"
            )

        except NoSuchElementException:
            return False
        else:
            return True

    def download_all_base64(self, driver):
        try:
            images = []
            while True:
                images.append(driver.find_element_by_xpath(
                    """//img[@id='page-scan-container']
                    [contains(@src,'data:image')]""")
                ).get_attribute("src")
                driver.find_element_by_xpath(
                    "//span[@aria-label='Next Page']").click()
        except NoSuchElementException:
            pass
        else:
            return images

    def clean_title(self, title):
        return title.translate(
            {ord(i): ord(" ") for i in punctuation})
